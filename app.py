# app.py
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB using the URI from .env
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database("healthTracker")  # Database name: healthTracker
collection = db.get_collection("entries")  # Collection name: entries

# Route for Dashboard
@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        # Collect data from form
        data = {
            "date": request.form["date"],
            "water": int(request.form["water"]),
            "calories": int(request.form["calories"]),
            "sleep": float(request.form["sleep"]),
            "exercise": request.form["exercise"]
        }
        # Insert data into MongoDB
        collection.insert_one(data)
        return redirect("/")  # Redirect to refresh page

    # Fetch all data from MongoDB
    all_data = list(collection.find())
    return render_template("dashboard.html", data=all_data)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
