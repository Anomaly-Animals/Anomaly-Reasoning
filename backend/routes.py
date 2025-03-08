from flask import Flask, request, jsonify
import reasoning_functions
import pandas as pd

app = Flask(__name__)


@app.route("/reasoning", methods=["POST"])
def get_reasoning_for_anomaly():
    if request.is_json:
        request_data = request.get_json()
        try:
            data = pd.read_csv("././data/datathon_data.csv")
        except Exception as e:
            return {
                "is_anomaly": False,
                "error": f"Error reading file: {str(e)}",
                "features": [],
            }

        # Filter data for the given BELNR
        entry = data[data["BELNR"] == request_data["anomaly_belnr"]]

        if entry.empty:
            return {
                "is_anomaly": False,
                "error": "No entry found with this BELNR",
                "features": [],
            }

        reasoning = reasoning_functions.check_anomaly_decision_tree(data, entry)

        return (
            jsonify({"message": "JSON received", "data": data, "reasoning": reasoning}),
            200,
        )
    else:
        return jsonify({"error": "Request must be JSON"}), 400
