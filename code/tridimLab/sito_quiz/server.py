from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

FILE_NAME = "data.json"

@app.route("/", methods=["POST"])
def handle_post():
    data = request.json  # Retrieve JSON data from the request
    print("Received data:", data)
    
    # Load existing data from the file
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                existing_data = json.load(file)  # Load current JSON data
            except json.JSONDecodeError:
                existing_data = []  # If the file is empty or corrupted, start fresh
    else:
        existing_data = []  # No file exists, start fresh
    
    # Append the new data to the existing data
    existing_data.append(data)
    
    # Save the updated data back to the file
    with open(FILE_NAME, "w") as file:
        json.dump(existing_data, file, indent=4)  # Write the updated JSON array

    return jsonify({"message": "Data received and appended to file!", "received": data})

if __name__ == "__main__":
    app.run(port=8000)
