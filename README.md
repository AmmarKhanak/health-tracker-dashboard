# Health Tracker Dashboard

A simple Health Tracker app built with Flask + MongoDB.

## Features
- Add daily health entries (water intake, calories, sleep, exercise)
- View all entries on a dashboard
- Data stored in MongoDB Atlas

## Technologies
- Flask
- MongoDB Atlas
- Python

## Setup Instructions

1. Clone this repo:
git clone https://github.com/yourusername/health-tracker-dashboard.git
cd health-tracker-dashboard


2. Create virtual environment & install dependencies:
python -m venv venv
source venv/bin/activate # Linux / Mac
venv\Scripts\activate # Windows

pip install -r requirements.txt


3. Add `.env` file:
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority

4. Run the app:

python app.py


5. Open browser:

http://127.0.0.1:5000/