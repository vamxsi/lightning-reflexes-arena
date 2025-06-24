# 5. Create .gitignore
gitignore_content = '''# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Build output
build/
dist/
.cache/
*.bundle.js

# Logs
logs
*.log

# Operating System Files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor directories and files
.idea/
.vscode/
*.swp
*.swo
*.sublime-workspace
*.sublime-project

# Testing
coverage/
.nyc_output/

# Temporary files
*.tmp
*.bak
*.swp
*.tgz

# Redis dump file
dump.rdb

# Deployment files
.vercel
.netlify

# Package manager lock files (uncomment if needed)
# package-lock.json
# yarn.lock
# pnpm-lock.yaml'''

with open('.gitignore', 'w') as f:
    f.write(gitignore_content)

print("✅ Created .gitignore")