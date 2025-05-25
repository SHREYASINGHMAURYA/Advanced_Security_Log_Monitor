from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Check if detection log exists
    log_path = "logs/detection_log.json"
    if os.path.exists(log_path):
        with open(log_path, "r") as file:
            detections = json.load(file)
    else:
        detections = []

    return render_template("dashboard.html", detections=detections)

@app.route("/api/detections")
def api_detections():
    log_path = "logs/detection_log.json"
    if os.path.exists(log_path):
        with open(log_path, "r") as file:
            detections = json.load(file)
    else:
        detections = []

    return jsonify(detections)

if __name__ == "__main__":
    app.run(debug=True)
