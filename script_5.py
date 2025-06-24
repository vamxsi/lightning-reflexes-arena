# 6. Create railway.json
railway_json = '''{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "npm start",
    "healthcheckPath": "/health",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 3
  }
}'''

with open('railway.json', 'w') as f:
    f.write(railway_json)

print("✅ Created railway.json")