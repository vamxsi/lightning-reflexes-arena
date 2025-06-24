# 9. Create GitHub Actions workflow
os.makedirs('.github/workflows', exist_ok=True)

deploy_yml = '''name: Deploy Lightning Reflexes Arena

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      redis:
        image: redis
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '16.x'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
  
  deploy-railway:
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Install Railway CLI
      run: npm i -g @railway/cli
    
    - name: Deploy to Railway
      run: railway up
      env:
        RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
  
  deploy-github-pages:
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '16.x'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Deploy to GitHub Pages
      run: |
        git config --global user.name ${{ github.actor }}
        git config --global user.email ${{ github.actor }}@users.noreply.github.com
        npm run deploy
      env:
        GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}'''

with open('.github/workflows/deploy.yml', 'w') as f:
    f.write(deploy_yml)

print("✅ Created .github/workflows/deploy.yml")