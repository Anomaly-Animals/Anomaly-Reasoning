from flask import Flask, request, jsonify
import reasoning_functions

app = Flask(__name__)


@app.route("/reasoning-for-anomaly", methods=["GET"])
def get_reasoning_for_anomaly():
    if request.is_json:
        data = request.get_json()
        reasoning = reasoning_functions.check_anomaly_decision_tree(
            data["anomaly_belnr"]
        )
        return (
            jsonify({"message": "JSON received", "data": data, "reasoning": reasoning}),
            200,
        )
    else:
        return jsonify({"error": "Request must be JSON"}), 400
