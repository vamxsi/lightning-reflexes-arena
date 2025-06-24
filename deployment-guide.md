# 🚀 Quick Deployment Guide: Lightning Reflexes Arena

## Method 1: Railway Deployment (RECOMMENDED - 5 minutes)

**Why Railway?** Built-in Redis, automatic deployments, free tier available.

### Steps:

1. **Create GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/lightning-reflexes-arena.git
   git push -u origin main
   ```

2. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add Redis database: Click "New" → "Database" → "Redis"
   - Railway will auto-deploy your game!

3. **Get Your Live URL**
   - Railway will provide a URL like: `https://lightning-reflexes-arena-production.up.railway.app`

**That's it! Your game is live in 5 minutes.**

---

## Method 2: Heroku Deployment (10 minutes)

### Steps:

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Deploy**
   ```bash
   heroku login
   heroku create lightning-reflexes-arena-$(date +%s)
   heroku addons:create heroku-redis:hobby-dev
   git push heroku main
   ```

3. **Get Your URL**
   ```bash
   heroku open
   ```

---

## Method 3: Local Development (2 minutes)

### Steps:

1. **Start Redis**
   ```bash
   # macOS
   brew services start redis
   
   # Docker (any OS)
   docker run -d -p 6379:6379 redis:alpine
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   ```

3. **Install & Run**
   ```bash
   npm install
   npm run dev
   ```

4. **Open Browser**
   - Go to `http://localhost:3000`

---

## Method 4: One-Click Automated (Using deploy.sh)

### Steps:

1. **Run Deployment Script**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Choose Option**
   - Select "1" for Railway
   - Select "2" for Heroku  
   - Select "4" for local development

**The script handles everything automatically!**

---

## Required Setup Before Playing

### 1. Install Backpack Wallet
- Go to [backpack.app](https://backpack.app)
- Install browser extension
- Create wallet

### 2. Get $GOR Tokens
- Visit Gorbagana faucet: [gorbaganachain.xyz](https://gorbaganachain.xyz)
- Connect your Backpack wallet
- Request test tokens

### 3. Configure Wallet for Gorbagana
- Network: Gorbagana Testnet
- RPC URL: `https://gorchain.wstf.io`

---

## Testing Your Live Game

### 1. Single Player Test
- Connect wallet
- Join quick match
- Wait for 30 seconds (game starts with 1 player for testing)

### 2. Multiplayer Test
- Open multiple browser tabs/windows
- Connect different wallets (or same wallet in different tabs)
- Join same game room
- Test real-time multiplayer

### 3. Blockchain Integration Test
- Verify wallet connection
- Check $GOR balance deduction (10 tokens per game)
- Confirm prize distribution after game

---

## Bounty Submission Checklist

### ✅ Technical Requirements
- [ ] Working live game URL
- [ ] GitHub repository with all code
- [ ] Backpack wallet integration
- [ ] Gorbagana testnet connectivity
- [ ] Multiplayer functionality (2-8 players)
- [ ] $GOR token integration
- [ ] Comprehensive README

### ✅ Social Media
- [ ] Create promotional tweet
- [ ] Include hashtag: #GorbaganaTestnet
- [ ] Tag: @Gorbagana_chain @sarv_shaktimaan @lex_node
- [ ] Include live game URL
- [ ] Share gameplay video/screenshots

### ✅ Tweet Template
```
🚀 Lightning Reflexes Arena is LIVE on @Gorbagana_chain testnet!

⚡ Multiplayer reaction game
🎮 Real-time competition
💰 $GOR token rewards  
🏆 Global leaderboard

Play now: [YOUR_LIVE_URL]

#GorbaganaTestnet @sarv_shaktimaan @lex_node

Built for the Gorbagana bounty! 🏅
```

---

## Troubleshooting

### Game Won't Load
- Check if server is running
- Verify all dependencies installed: `npm install`
- Check browser console for errors

### Wallet Won't Connect
- Install Backpack wallet extension
- Configure Gorbagana testnet settings
- Refresh page and try again

### Redis Errors
- Local: `brew services start redis`
- Cloud: Verify Redis addon is active
- Check REDIS_URL environment variable

### Multiplayer Not Working
- Check WebSocket connection
- Verify server is publicly accessible
- Test with multiple browser windows

---

## Performance Tips

### For Best Results:
- Use Railway or Heroku for hosting (not local)
- Test with 4-6 players for optimal experience
- Ensure stable internet connection
- Use Chrome/Firefox for best compatibility

### Game Features to Highlight:
- Sub-100ms reaction time accuracy
- Instant blockchain transactions
- Real-time leaderboard updates
- Cross-platform compatibility
- Professional game design

---

**Ready to win the bounty? Deploy now and start testing!** 🎯