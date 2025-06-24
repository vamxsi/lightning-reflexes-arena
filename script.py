# Create all required files for Lightning Reflexes Arena game

# 1. package.json
package_json = '''{
  "name": "lightning-reflexes-arena",
  "version": "1.0.0",
  "description": "Multiplayer reaction game for Gorbagana testnet bounty",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "build": "echo 'Building project...'",
    "test": "echo 'Running tests...'",
    "deploy": "gh-pages -d public"
  },
  "keywords": [
    "game",
    "multiplayer",
    "blockchain",
    "gorbagana",
    "solana"
  ],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "socket.io": "^4.7.2",
    "redis": "^4.6.8",
    "@solana/web3.js": "^1.87.6",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "gh-pages": "^6.0.0"
  },
  "engines": {
    "node": ">=16.0.0"
  }
}'''

# Write package.json
with open('package.json', 'w') as f:
    f.write(package_json)

print("✅ Created package.json")