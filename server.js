const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const redis = require('redis');
const path = require('path');
const cors = require('cors');
require('dotenv').config();

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Redis setup
let redisClient;
if (process.env.REDIS_URL) {
  redisClient = redis.createClient({ url: process.env.REDIS_URL });
} else {
  redisClient = redis.createClient();
}
redisClient.connect().catch(console.error);

// Game state
const gameRooms = new Map();
const playerSockets = new Map();

// Game configuration
const GAME_CONFIG = {
  MAX_PLAYERS: 8,
  ENTRY_FEE: 10,
  ROUND_DURATION: 30000,
  CHALLENGE_TYPES: ['color', 'audio', 'shape', 'chaos']
};

// Socket handling
io.on('connection', (socket) => {
  console.log('Player connected:', socket.id);

  socket.on('join-game', async (data) => {
    const { playerAddress, gameMode } = data;

    // Find or create game room
    let roomId = await findAvailableRoom(gameMode);
    if (!roomId) {
      roomId = createNewRoom(gameMode);
    }

    // Add player to room
    socket.join(roomId);
    playerSockets.set(socket.id, { roomId, playerAddress });

    const room = gameRooms.get(roomId);
    room.players.push({
      socketId: socket.id,
      address: playerAddress,
      score: 0,
      ready: false
    });

    socket.emit('room-joined', { roomId, players: room.players });
    socket.to(roomId).emit('player-joined', { players: room.players });

    // Check if game can start
    if (room.players.length >= 2) {
      setTimeout(() => startGame(roomId), 3000);
    }
  });

  socket.on('player-reaction', async (data) => {
    const { reactionTime, challengeType } = data;
    const playerInfo = playerSockets.get(socket.id);

    if (playerInfo) {
      const room = gameRooms.get(playerInfo.roomId);
      const player = room.players.find(p => p.socketId === socket.id);

      if (player) {
        const score = Math.max(100, 1000 - reactionTime);
        player.score += score;

        // Broadcast reaction result
        io.to(playerInfo.roomId).emit('reaction-result', {
          playerId: socket.id,
          reactionTime,
          score,
          totalScore: player.score
        });
      }
    }
  });

  socket.on('disconnect', () => {
    console.log('Player disconnected:', socket.id);
    handlePlayerDisconnect(socket.id);
  });
});

async function findAvailableRoom(gameMode) {
  for (let [roomId, room] of gameRooms) {
    if (room.gameMode === gameMode && 
        room.status === 'waiting' && 
        room.players.length < GAME_CONFIG.MAX_PLAYERS) {
      return roomId;
    }
  }
  return null;
}

function createNewRoom(gameMode) {
  const roomId = `room_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`;
  gameRooms.set(roomId, {
    id: roomId,
    gameMode,
    players: [],
    status: 'waiting',
    currentRound: 0,
    startTime: null
  });
  return roomId;
}

function startGame(roomId) {
  const room = gameRooms.get(roomId);
  if (!room || room.players.length < 2) return;

  room.status = 'playing';
  room.startTime = Date.now();
  room.currentRound = 1;

  io.to(roomId).emit('game-started', {
    players: room.players,
    round: room.currentRound
  });

  // Start first challenge
  setTimeout(() => sendChallenge(roomId), 2000);
}

function sendChallenge(roomId) {
  const room = gameRooms.get(roomId);
  if (!room || room.status !== 'playing') return;

  const challengeType = GAME_CONFIG.CHALLENGE_TYPES[
    Math.floor(Math.random() * GAME_CONFIG.CHALLENGE_TYPES.length)
  ];
  const challenge = generateChallenge(challengeType);

  io.to(roomId).emit('new-challenge', challenge);

  // Next challenge after delay
  setTimeout(() => {
    if (room.currentRound < 10) {
      room.currentRound++;
      sendChallenge(roomId);
    } else {
      endGame(roomId);
    }
  }, 5000);
}

function generateChallenge(type) {
  const challenges = {
    color: {
      type: 'color',
      stimulus: '#00ff00',
      instruction: 'Click when screen turns GREEN!',
      delay: Math.random() * 3000 + 1000
    },
    audio: {
      type: 'audio',
      frequency: 440,
      instruction: 'Click when you hear the tone!',
      delay: Math.random() * 3000 + 1000
    },
    shape: {
      type: 'shape',
      shape: 'circle',
      instruction: 'Click when you see a CIRCLE!',
      delay: Math.random() * 3000 + 1000
    },
    chaos: {
      type: 'chaos',
      instruction: 'React to any stimulus!',
      delay: Math.random() * 2000 + 500
    }
  };

  return challenges[type];
}

function endGame(roomId) {
  const room = gameRooms.get(roomId);
  if (!room) return;

  room.status = 'finished';

  // Sort players by score
  const rankings = room.players
    .sort((a, b) => b.score - a.score)
    .map((player, index) => ({
      ...player,
      rank: index + 1
    }));

  io.to(roomId).emit('game-ended', { rankings });

  // Update leaderboard
  updateLeaderboard(rankings);

  // Clean up room after delay
  setTimeout(() => {
    gameRooms.delete(roomId);
  }, 30000);
}

async function updateLeaderboard(rankings) {
  try {
    for (let player of rankings) {
      await redisClient.zAdd('leaderboard', [
        { score: player.score, value: player.address }
      ]);
    }
  } catch (error) {
    console.error('Error updating leaderboard:', error);
  }
}

function handlePlayerDisconnect(socketId) {
  const playerInfo = playerSockets.get(socketId);
  if (playerInfo) {
    const room = gameRooms.get(playerInfo.roomId);
    if (room) {
      room.players = room.players.filter(p => p.socketId !== socketId);
      io.to(playerInfo.roomId).emit('player-left', { players: room.players });
    }
    playerSockets.delete(socketId);
  }
}

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// API routes
app.get('/api/leaderboard', async (req, res) => {
  try {
    const top10 = await redisClient.zRangeWithScores('leaderboard', 0, 9, { REV: true });
    res.json(top10);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch leaderboard' });
  }
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Lightning Reflexes Arena server running on port ${PORT}`);
});