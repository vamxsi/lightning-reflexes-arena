# 4. Create .env.example
env_example = '''# Lightning Reflexes Arena Environment Variables

# Server Configuration
PORT=3000
NODE_ENV=production

# Redis Configuration
# Replace with your Redis URL in production
REDIS_URL=redis://localhost:6379

# Gorbagana Testnet Configuration
GORBAGANA_RPC_URL=https://gorchain.wstf.io
GORBAGANA_WEBSOCKET_URL=wss://gorchain.wstf.io

# Game Settings
MAX_PLAYERS=8
ENTRY_FEE=10
ROUND_DURATION=30000

# Deployment Settings
# Uncomment and set these for your production deployment
# DOMAIN_NAME=your-game-domain.com
# SSL_ENABLED=true'''

with open('.env.example', 'w') as f:
    f.write(env_example)

print("✅ Created .env.example")