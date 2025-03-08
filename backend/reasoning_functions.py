def check_anomaly_decision_tree(data, entry):
    anomaly_features = []
    is_anomaly = False

    # Check for uniqueness in HKONT, BSCHL, or KTOSL
    for field in ["HKONT", "BSCHL", "KTOSL"]:
        if field in data.columns:
            field_value = entry[field].values[0]
            if len(data[data[field] == field_value]) == 1:
                is_anomaly = True
                anomaly_features.append(
                    {
                        "feature": field,
                        "value": str(field_value),
                        "reason": f"The value {field_value} didn't appear before in any entry of the field {field}. You may want to check this entry.",
                    }
                )

    # Check for specific DMBTR and WRBTR ranges (first range)
    if (
        entry["DMBTR"].values[0] > 910000
        and entry["DMBTR"].values[0] < 911000
        and entry["WRBTR"].values[0] > 54000
        and entry["WRBTR"].values[0] < 55000
    ):

        is_anomaly = True
        anomaly_features.append(
            {
                "feature": "DMBTR_WRBTR_RANGE_1",
                "value": f"DMBTR={entry['DMBTR'].values[0]}, WRBTR={entry['WRBTR'].values[0]}",
                "reason": f"The values for DMBTR ({entry['DMBTR'].values[0]}) and WRBTR ({entry['WRBTR'].values[0]}) fall into a range that was typical for previous anomalies (DMBTR: 910000-911000, WRBTR: 54000-55000). You may want to check this entry.",
            }
        )

    # Check for specific DMBTR and WRBTR ranges (second range)
    if (
        entry["DMBTR"].values[0] > 92445000
        and entry["DMBTR"].values[0] < 92446000
        and entry["WRBTR"].values[0] > 59585000
        and entry["WRBTR"].values[0] < 59586000
    ):

        is_anomaly = True
        anomaly_features.append(
            {
                "feature": "DMBTR_WRBTR_RANGE_2",
                "value": f"DMBTR={entry['DMBTR'].values[0]}, WRBTR={entry['WRBTR'].values[0]}",
                "reason": f"The values for DMBTR ({entry['DMBTR'].values[0]}) and WRBTR ({entry['WRBTR'].values[0]}) fall into a range that was typical for previous anomalies (DMBTR: 92445000-92446000, WRBTR: 59585000-59586000). You may want to check this entry.",
            }
        )

    result = {"is_anomaly": is_anomaly, "anomaly_features": anomaly_features}

    # Find previous and next anomalies if current entry is an anomaly
    if is_anomaly:

        # Sort the data by BELNR to find previous and next anomalies
        sorted_data = data.sort_values(by="BELNR").reset_index(drop=True)

        # Find current position in sorted anomalies list
        print(f"BELNR123: {entry['BELNR'].values[0]}")
        current_index = sorted_data[
            sorted_data["BELNR"] == entry["BELNR"].values[0]
        ].index[0]

        # Check and assign previous and next BELNR if they exist
        previous_belnr = (
            sorted_data.loc[current_index - 1, "BELNR"] if current_index > 0 else None
        )
        next_belnr = (
            sorted_data.loc[current_index + 1, "BELNR"]
            if current_index < len(sorted_data) - 1
            else None
        )

        # Add previous and next anomaly information
        result["previous_anomaly_belnr"] = previous_belnr
        result["next_anomaly_belnr"] = next_belnr

    if not is_anomaly:
        result["message"] = "No anomalies detected"

    return result
