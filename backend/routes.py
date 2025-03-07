from flask import Flask, request, jsonify
import pandas as pd
import reasoning_functions

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/reasoning-for-anomaly", methods=["GET"])
def get_reasoning_for_anomaly():
    if request.is_json:
        data = request.get_json()
        reasoning = reasoning_functions.max(data["anomaly_id"])
        return (
            jsonify({"message": "JSON received", "data": data, "reasoning": reasoning}),
            200,
        )
    else:
        return jsonify({"error": "Request must be JSON"}), 400
