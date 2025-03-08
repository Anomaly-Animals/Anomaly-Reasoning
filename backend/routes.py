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
        belnr = str(request_data["anomaly_belnr"]).strip()  # Ensure belnr is a string and remove any whitespace
        data['BELNR'] = data['BELNR'].astype(str).str.strip()  # Ensure BELNR is a string and stripped
        entry = data[data["BELNR"] == belnr]

        if entry.empty:
            return {
                "is_anomaly": False,
                "error": "No entry found with this BELNR",
                "features": [],
            }

        reasoning = reasoning_functions.check_anomaly_decision_tree(data, entry)

         # Convert 'entry' (which is a DataFrame) to a dictionary, suitable for JSON response
        entry_dict = entry.to_dict(orient='records')  # Convert the DataFrame to a list of dicts (one per row)

        return jsonify({
            "message": "JSON received",
            "data": entry_dict,  # Return 'entry' as a list of dicts
            "reasoning": reasoning
        }), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400
