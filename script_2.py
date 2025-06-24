# 3. Create the public directory and index.html file
import os

# Create public directory if it doesn't exist
os.makedirs('public', exist_ok=True)

# Complete HTML file with game interface
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lightning Reflexes Arena - Gorbagana Testnet</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            flex: 1;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .wallet-section {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }

        .btn {
            background: linear-gradient(45deg, #ff6b6b, #ff8e53);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 5px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .game-area {
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            min-height: 400px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: all 0.3s ease;
        }

        .game-area.active {
            background: rgba(255,255,255,0.2);
            transform: scale(1.02);
        }

        .challenge-area {
            font-size: 2rem;
            margin: 20px 0;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .scoreboard {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
        }

        .player-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 15px;
        }

        .player-item {
            background: rgba(255,255,255,0.1);
            padding: 10px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .status {
            padding: 10px;
            margin: 10px 0;
            border-radius: 10px;
            background: rgba(255,255,255,0.1);
        }

        .leaderboard {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
        }

        .leaderboard-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }

        .reaction-circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: #ff6b6b;
            margin: 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1.5rem;
            font-weight: bold;
        }

        .reaction-circle.active {
            background: #00ff00;
            transform: scale(1.1);
        }

        .reaction-circle:hover {
            transform: scale(1.05);
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 10px;
            }
            
            .reaction-circle {
                width: 150px;
                height: 150px;
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>⚡ Lightning Reflexes Arena</h1>
            <p class="subtitle">Multiplayer Blockchain Reaction Game on Gorbagana Testnet</p>
        </header>

        <div class="wallet-section">
            <h3>🔗 Wallet Connection</h3>
            <div id="wallet-status">
                <button id="connect-wallet-btn" class="btn">Connect Backpack Wallet</button>
                <p id="wallet-info"></p>
            </div>
        </div>

        <div class="game-area" id="game-area">
            <div id="game-menu">
                <h2>🎮 Game Menu</h2>
                <p>Entry Fee: 10 $GOR | Prize Pool: 60% Winner, 25% 2nd, 15% 3rd</p>
                <button id="join-game-btn" class="btn" disabled>Join Quick Match</button>
                <button id="create-room-btn" class="btn" disabled>Create Private Room</button>
            </div>

            <div id="game-lobby" style="display: none;">
                <h2>🏟️ Game Lobby</h2>
                <p id="lobby-info"></p>
                <div id="players-list" class="player-list"></div>
                <div id="game-countdown"></div>
            </div>

            <div id="game-play" style="display: none;">
                <h2 id="game-instruction">Get Ready!</h2>
                <div id="challenge-area" class="challenge-area">
                    <div id="reaction-circle" class="reaction-circle">
                        Wait...
                    </div>
                </div>
                <div id="game-stats">
                    <p>Round: <span id="current-round">1</span>/10</p>
                    <p>Your Score: <span id="player-score">0</span></p>
                </div>
            </div>

            <div id="game-results" style="display: none;">
                <h2>🏆 Game Results</h2>
                <div id="final-rankings"></div>
                <button id="play-again-btn" class="btn">Play Again</button>
            </div>
        </div>

        <div class="scoreboard">
            <h3>📊 Live Scoreboard</h3>
            <div id="live-scores"></div>
        </div>

        <div class="leaderboard">
            <h3>🏅 Global Leaderboard</h3>
            <div id="leaderboard-list"></div>
        </div>

        <div class="status" id="connection-status">
            <p>🔴 Not Connected</p>
        </div>
    </div>

    <script src="/socket.io/socket.io.js"></script>
    <script src="https://unpkg.com/@solana/web3.js@latest/lib/index.iife.js"></script>
    <script>
        // Game state
        let socket;
        let wallet = null;
        let gameState = 'menu';
        let currentChallenge = null;
        let reactionStartTime = 0;
        let playerScore = 0;
        let currentRound = 1;

        // DOM elements
        const connectWalletBtn = document.getElementById('connect-wallet-btn');
        const walletInfo = document.getElementById('wallet-info');
        const joinGameBtn = document.getElementById('join-game-btn');
        const createRoomBtn = document.getElementById('create-room-btn');
        const gameMenu = document.getElementById('game-menu');
        const gameLobby = document.getElementById('game-lobby');
        const gamePlay = document.getElementById('game-play');
        const gameResults = document.getElementById('game-results');
        const reactionCircle = document.getElementById('reaction-circle');
        const gameInstruction = document.getElementById('game-instruction');
        const connectionStatus = document.getElementById('connection-status');

        // Initialize socket connection
        function initSocket() {
            socket = io();
            
            socket.on('connect', () => {
                connectionStatus.innerHTML = '<p>🟢 Connected to Server</p>';
            });

            socket.on('disconnect', () => {
                connectionStatus.innerHTML = '<p>🔴 Disconnected from Server</p>';
            });

            socket.on('room-joined', (data) => {
                showLobby(data);
            });

            socket.on('player-joined', (data) => {
                updatePlayersList(data.players);
            });

            socket.on('game-started', (data) => {
                startGamePlay();
            });

            socket.on('new-challenge', (challenge) => {
                handleNewChallenge(challenge);
            });

            socket.on('reaction-result', (data) => {
                handleReactionResult(data);
            });

            socket.on('game-ended', (data) => {
                showResults(data.rankings);
            });
        }

        // Wallet connection
        connectWalletBtn.addEventListener('click', async () => {
            try {
                if (window.backpack && window.backpack.isBackpack) {
                    await window.backpack.connect();
                    wallet = window.backpack;
                    const publicKey = await wallet.getAccount();
                    walletInfo.innerHTML = `Connected: ${publicKey.toString().slice(0, 8)}...`;
                    joinGameBtn.disabled = false;
                    createRoomBtn.disabled = false;
                    connectWalletBtn.style.display = 'none';
                } else {
                    alert('Please install Backpack wallet extension');
                }
            } catch (error) {
                console.error('Wallet connection failed:', error);
                alert('Failed to connect wallet');
            }
        });

        // Game controls
        joinGameBtn.addEventListener('click', () => {
            if (wallet) {
                joinGame();
            }
        });

        createRoomBtn.addEventListener('click', () => {
            if (wallet) {
                createRoom();
            }
        });

        // Game functions
        async function joinGame() {
            try {
                const publicKey = await wallet.getAccount();
                socket.emit('join-game', {
                    playerAddress: publicKey.toString(),
                    gameMode: 'quick'
                });
            } catch (error) {
                console.error('Failed to join game:', error);
            }
        }

        async function createRoom() {
            try {
                const publicKey = await wallet.getAccount();
                socket.emit('join-game', {
                    playerAddress: publicKey.toString(),
                    gameMode: 'private'
                });
            } catch (error) {
                console.error('Failed to create room:', error);
            }
        }

        function showLobby(data) {
            gameMenu.style.display = 'none';
            gameLobby.style.display = 'block';
            document.getElementById('lobby-info').textContent = `Room: ${data.roomId}`;
            updatePlayersList(data.players);
        }

        function updatePlayersList(players) {
            const playersList = document.getElementById('players-list');
            playersList.innerHTML = '';
            
            players.forEach((player, index) => {
                const playerItem = document.createElement('div');
                playerItem.className = 'player-item';
                playerItem.innerHTML = `
                    <span>Player ${index + 1}</span>
                    <span>${player.address.slice(0, 8)}...</span>
                `;
                playersList.appendChild(playerItem);
            });
        }

        function startGamePlay() {
            gameLobby.style.display = 'none';
            gamePlay.style.display = 'block';
            gameState = 'playing';
            
            // Reset scores
            playerScore = 0;
            currentRound = 1;
            updateGameStats();
        }

        function handleNewChallenge(challenge) {
            currentChallenge = challenge;
            gameInstruction.textContent = challenge.instruction;
            reactionCircle.textContent = 'Wait...';
            reactionCircle.classList.remove('active');
            
            // Show stimulus after delay
            setTimeout(() => {
                showStimulus(challenge);
            }, challenge.delay);
        }

        function showStimulus(challenge) {
            reactionStartTime = Date.now();
            
            switch (challenge.type) {
                case 'color':
                    reactionCircle.style.background = challenge.stimulus;
                    reactionCircle.classList.add('active');
                    reactionCircle.textContent = 'CLICK!';
                    break;
                case 'audio':
                    playTone(challenge.frequency);
                    reactionCircle.classList.add('active');
                    reactionCircle.textContent = 'CLICK!';
                    break;
                case 'shape':
                    reactionCircle.classList.add('active');
                    reactionCircle.textContent = '●';
                    break;
                case 'chaos':
                    reactionCircle.classList.add('active');
                    reactionCircle.textContent = 'NOW!';
                    break;
            }
        }

        // Reaction handling
        reactionCircle.addEventListener('click', () => {
            if (gameState === 'playing' && reactionStartTime > 0) {
                const reactionTime = Date.now() - reactionStartTime;
                socket.emit('player-reaction', {
                    reactionTime: reactionTime,
                    challengeType: currentChallenge.type
                });
                
                // Reset for next challenge
                reactionStartTime = 0;
                reactionCircle.classList.remove('active');
                reactionCircle.style.background = '#ff6b6b';
                reactionCircle.textContent = 'Wait...';
            }
        });

        function handleReactionResult(data) {
            if (data.playerId === socket.id) {
                playerScore = data.totalScore;
                updateGameStats();
                
                // Show reaction time feedback
                setTimeout(() => {
                    gameInstruction.textContent = `Reaction: ${data.reactionTime}ms (+${data.score} points)`;
                }, 500);
            }
        }

        function updateGameStats() {
            document.getElementById('current-round').textContent = currentRound;
            document.getElementById('player-score').textContent = playerScore;
        }

        function showResults(rankings) {
            gamePlay.style.display = 'none';
            gameResults.style.display = 'block';
            
            const finalRankings = document.getElementById('final-rankings');
            finalRankings.innerHTML = '';
            
            rankings.forEach(player => {
                const rankItem = document.createElement('div');
                rankItem.className = 'leaderboard-item';
                rankItem.innerHTML = `
                    <span>#${player.rank} ${player.address.slice(0, 8)}...</span>
                    <span>${player.score} points</span>
                `;
                finalRankings.appendChild(rankItem);
            });
        }

        // Audio functions
        function playTone(frequency) {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = frequency;
            oscillator.type = 'sine';
            gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
            
            oscillator.start();
            oscillator.stop(audioContext.currentTime + 0.5);
        }

        // Play again
        document.getElementById('play-again-btn').addEventListener('click', () => {
            gameResults.style.display = 'none';
            gameMenu.style.display = 'block';
            gameState = 'menu';
        });

        // Load leaderboard
        async function loadLeaderboard() {
            try {
                const response = await fetch('/api/leaderboard');
                const leaderboard = await response.json();
                
                const leaderboardList = document.getElementById('leaderboard-list');
                leaderboardList.innerHTML = '';
                
                leaderboard.forEach((entry, index) => {
                    const item = document.createElement('div');
                    item.className = 'leaderboard-item';
                    item.innerHTML = `
                        <span>#${index + 1} ${entry.value.slice(0, 8)}...</span>
                        <span>${entry.score} points</span>
                    `;
                    leaderboardList.appendChild(item);
                });
            } catch (error) {
                console.error('Failed to load leaderboard:', error);
            }
        }

        // Initialize app
        document.addEventListener('DOMContentLoaded', () => {
            initSocket();
            loadLeaderboard();
            
            // Auto-detect wallet
            if (window.backpack && window.backpack.isBackpack) {
                connectWalletBtn.style.display = 'block';
            } else {
                walletInfo.innerHTML = '<p>Please install Backpack wallet extension</p>';
            }
        });
    </script>
</body>
</html>'''

# Write index.html
with open('public/index.html', 'w') as f:
    f.write(index_html)

print("✅ Created public/index.html")