# Lab Reports Analysis API

This is a Flask-based API for analyzing lab reports.

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Python Version: 3.9 or later

## Environment Variables

No environment variables are required for basic setup.

## API Endpoints

- GET `/`: Home endpoint
- POST `/predict`: Prediction endpoint (Send JSON data)

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The server will start at http://localhost:10000
