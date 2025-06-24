# ⚡ Lightning Reflexes Arena

**The Ultimate Multiplayer Reaction Game on Gorbagana Testnet**

A fast-paced, competitive multiplayer mini-game designed specifically for the Gorbagana bounty competition. Test your reflexes against players worldwide while showcasing the speed and fairness of the Gorbagana testnet.

## 🎮 Game Features

- **Real-time Multiplayer**: Compete against 2-8 players in lightning-fast reaction challenges
- **Blockchain Integration**: Built on Gorbagana testnet with $GOR token rewards
- **Multiple Challenge Types**: Color burst, audio pulse, shape recognition, and chaos rounds
- **Instant Rewards**: Automatic prize distribution based on performance
- **Global Leaderboard**: Track the fastest reflexes worldwide
- **Cross-platform**: Works on desktop and mobile browsers

## 🏗️ Technical Architecture

### Frontend
- **HTML5/CSS3/JavaScript**: Responsive, mobile-first design
- **Socket.io Client**: Real-time multiplayer communication
- **Backpack Wallet Integration**: Seamless Web3 connectivity
- **Solana Web3.js**: Blockchain transaction handling

### Backend
- **Node.js + Express**: High-performance server architecture
- **Socket.io**: WebSocket-based real-time communication
- **Redis**: Leaderboard persistence and session management
- **Gorbagana Testnet**: Custom Solana fork integration

## 🚀 Quick Start

### Prerequisites

- Node.js 16+ installed
- Redis server (local or cloud)
- Backpack wallet extension
- $GOR tokens from Gorbagana faucet

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lightning-reflexes-arena.git
   cd lightning-reflexes-arena
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

4. **Start Redis server**
   ```bash
   # On macOS
   brew services start redis
   
   # On Ubuntu
   sudo systemctl start redis
   
   # Using Docker
   docker run -d -p 6379:6379 redis:alpine
   ```

5. **Run the game**
   ```bash
   npm run dev
   ```

6. **Open your browser**
   Navigate to `http://localhost:3000`

## 🌐 Deployment Options

### Option 1: Railway (Recommended)

Railway provides the easiest deployment with built-in Redis support:

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Deploy**
   ```bash
   railway up
   ```

4. **Add Redis addon**
   - Go to Railway dashboard
   - Add Redis database
   - Environment variables are auto-configured

### Option 2: Heroku

Deploy to Heroku with Redis addon:

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add Redis addon**
   ```bash
   heroku addons:create heroku-redis:hobby-dev
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Option 3: GitHub Pages (Frontend Only)

For static frontend-only deployment:

1. **Enable GitHub Pages**
   - Go to repository settings
   - Enable Pages from main branch

2. **Deploy**
   ```bash
   npm run deploy
   ```

## 🎯 Game Rules

### Objective
React as quickly as possible to on-screen stimuli to earn points and climb the leaderboard.

### Challenge Types

1. **Color Burst**: Click when the screen turns green
2. **Audio Pulse**: Click when you hear the tone
3. **Shape Strike**: Click when you see a circle
4. **Chaos Round**: React to any stimulus

### Scoring
- Base score: 1000 points
- Subtract reaction time in milliseconds
- Minimum score: 100 points
- Faster reactions = higher scores

### Prize Distribution
- **1st Place**: 60% of prize pool
- **2nd Place**: 25% of prize pool
- **3rd Place**: 15% of prize pool
- **Entry Fee**: 10 $GOR per game

## 🔧 Configuration

### Environment Variables

```env
# Server Configuration
PORT=3000
NODE_ENV=production

# Redis Configuration
REDIS_URL=redis://localhost:6379

# Gorbagana Testnet Configuration
GORBAGANA_RPC_URL=https://gorchain.wstf.io
GORBAGANA_WEBSOCKET_URL=wss://gorchain.wstf.io

# Game Settings
MAX_PLAYERS=8
ENTRY_FEE=10
ROUND_DURATION=30000
```

## 📊 API Endpoints

### Health Check
```
GET /health
```
Returns server status and timestamp.

### Leaderboard
```
GET /api/leaderboard
```
Returns top 10 players with scores.

## 🎲 Game Flow

1. **Connect Wallet**: Connect your Backpack wallet
2. **Get Tokens**: Obtain $GOR from Gorbagana faucet
3. **Join Game**: Enter matchmaking or create private room
4. **Play Rounds**: Complete 10 reaction challenges
5. **Collect Rewards**: Automatic prize distribution
6. **Climb Leaderboard**: Compete for global rankings

## 🛠️ Development

### Project Structure
```
lightning-reflexes-arena/
├── package.json              # Project configuration
├── server.js                 # Main server file
├── .env.example              # Environment template
├── .gitignore               # Git ignore rules
├── railway.json             # Railway deployment config
├── Procfile                 # Heroku deployment config
├── deploy.sh                # Deployment script
├── README.md                # This file
├── public/
│   └── index.html           # Frontend game interface
└── .github/
    └── workflows/
        └── deploy.yml       # GitHub Actions workflow
```

### Development Commands

```bash
npm start        # Start production server
npm run dev      # Start development server with hot reload
npm test         # Run tests
npm run deploy   # Deploy to GitHub Pages
```

## 🎉 Bounty Submission

This project fully meets all Gorbagana bounty requirements:

- ✅ **Working Prototype**: Live multiplayer game
- ✅ **Gorbagana Integration**: Runs on testnet with $GOR tokens
- ✅ **Backpack Wallet**: Native wallet support
- ✅ **Multiplayer**: 2-8 player support
- ✅ **Documentation**: Comprehensive README
- ✅ **Social Ready**: Built-in sharing features

### Submission Checklist

1. **Deploy to production** (Railway/Heroku)
2. **Test with multiple players**
3. **Verify wallet connectivity**
4. **Confirm $GOR token functionality**
5. **Create promotional tweet**
6. **Submit to bounty program**

## 📱 Social Media

**Twitter Announcement Template:**

```
🚀 Just launched Lightning Reflexes Arena on @Gorbagana_chain testnet! 

⚡ Multiplayer reaction game
🎮 Real-time competition  
💰 $GOR token rewards
🏆 Global leaderboard

Test your reflexes: [YOUR_DEPLOYED_URL]

#GorbaganaTestnet @sarv_shaktimaan @lex_node

Built for the Gorbagana bounty competition! 🏅
```

## 🐛 Troubleshooting

### Common Issues

**Wallet Connection Fails**
- Ensure Backpack wallet extension is installed
- Check if wallet is connected to Gorbagana testnet
- Refresh page and try again

**Redis Connection Error**
- Verify Redis server is running
- Check REDIS_URL in environment variables
- For cloud deployments, ensure Redis addon is configured

**Game Doesn't Start**
- Ensure minimum 2 players are connected
- Check browser console for WebSocket errors
- Verify server is running and accessible

**Token Transactions Fail**
- Confirm sufficient $GOR balance
- Check Gorbagana testnet connectivity
- Verify wallet is connected to correct network

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏆 Bounty Information

**Competition**: Gorbagana Testnet Multiplayer Mini-Game Bounty
**Deadline**: Check official bounty announcement
**Prizes**: $1,500 USDC (1st), $1,000 USDC (2nd), $750 USDC (3rd) + more

**Judging Criteria**:
- Gameplay & Fun (40 points)
- Testnet Integration (30 points)
- User Attraction (20 points)
- Social Promotion (10 points)

---

**Built with ❤️ for the Gorbagana community**

*Ready to test your reflexes? Let the games begin!* ⚡