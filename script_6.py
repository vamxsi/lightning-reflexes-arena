# 7. Create Procfile
procfile_content = '''web: npm start
worker: node server.js'''

with open('Procfile', 'w') as f:
    f.write(procfile_content)

print("✅ Created Procfile")