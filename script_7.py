# 8. Create deploy.sh script
deploy_sh = '''#!/bin/bash

# Lightning Reflexes Arena Deployment Script
echo "🚀 Lightning Reflexes Arena Deployment Script"
echo "============================================="

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
NC='\\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check prerequisites
echo "Checking prerequisites..."

# Check Node.js
if ! command -v node &> /dev/null; then
    print_error "Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 16 ]; then
    print_error "Node.js version must be 16 or higher. Current: $(node --version)"
    exit 1
fi

print_status "Node.js version: $(node --version)"

# Check npm
if ! command -v npm &> /dev/null; then
    print_error "npm is not installed."
    exit 1
fi

print_status "npm version: $(npm --version)"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    print_error "Failed to install dependencies"
    exit 1
fi

print_status "Dependencies installed successfully"

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating environment configuration..."
    cp .env.example .env
    print_warning "Please edit .env file with your configurations"
fi

# Deployment options
echo ""
echo "🌐 Choose deployment option:"
echo "1) Railway (Recommended)"
echo "2) Heroku"
echo "3) GitHub Pages (Frontend only)"
echo "4) Local development server"
echo "5) Exit"

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🚂 Deploying to Railway..."
        if ! command -v railway &> /dev/null; then
            print_warning "Installing Railway CLI..."
            npm install -g @railway/cli
        fi
        
        print_status "Railway CLI installed"
        echo "Please run 'railway login' and 'railway up' to deploy"
        ;;
    2)
        echo ""
        echo "🟣 Deploying to Heroku..."
        if ! command -v heroku &> /dev/null; then
            print_error "Heroku CLI not found. Please install Heroku CLI first."
            exit 1
        fi
        
        heroku create lightning-reflexes-arena-$(date +%s)
        heroku addons:create heroku-redis:hobby-dev
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        ;;
    3)
        echo ""
        echo "📄 Deploying to GitHub Pages..."
        npm run deploy
        ;;
    4)
        echo ""
        echo "💻 Starting local development server..."
        print_warning "Make sure Redis is running locally"
        npm run dev
        ;;
    5)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        print_error "Invalid choice"
        exit 1
        ;;
esac'''

with open('deploy.sh', 'w') as f:
    f.write(deploy_sh)

# Make deploy.sh executable
import stat
st = os.stat('deploy.sh')
os.chmod('deploy.sh', st.st_mode | stat.S_IEXEC)

print("✅ Created deploy.sh (executable)")