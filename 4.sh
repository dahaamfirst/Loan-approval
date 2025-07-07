# أنشئ ملف package.json أساسي إذا كان مفقوداً
echo '{
  "name": "loan_approval",
  "version": "1.0.0",
  "scripts": {
    "build": "your-build-command"
  }
}' > package.json