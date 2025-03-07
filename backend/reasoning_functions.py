from abc import abstractmethod
import json
import pandas as pd


@abstractmethod
def _get_reasoning_for_anomaly(anomaly_belnr) -> json:
    """
    Abstract method to get reasoning for a given anomaly.

    Parameters:
    anomaly_belnr (Any): The anomaly for which reasoning is to be provided.

    Returns:
    Any: The reasoning for the given anomaly.
    """
    pass

def check_anomaly(belnr):
    """
    Checks if an entry with the given BELNR is an anomaly based on specific criteria.
    
    Parameters:
    belnr (str): The BELNR value to check for anomalies
    
    Returns:
    dict: JSON-compatible dictionary with anomaly information
    """
    # Load data from CSV file
    try:
        data = pd.read_csv('././data/datathon_data.csv')
    except Exception as e:
        return {"is_anomaly": False, "error": f"Error reading file: {str(e)}", "features": []}
    
    # Filter data for the given BELNR
    entry = data[data['BELNR'] == belnr]
    
    if entry.empty:
        return {"is_anomaly": False, "error": "No entry found with this BELNR", "features": []}
    
    anomaly_features = []
    is_anomaly = False
    
    # Check for uniqueness in HKONT, BSCHL, or KTOSL
    for field in ['HKONT', 'BSCHL', 'KTOSL']:
        if field in data.columns:
            field_value = entry[field].values[0]
            if len(data[data[field] == field_value]) == 1:
                is_anomaly = True
                anomaly_features.append({
                    "feature": field,
                    "value": str(field_value),
                    "reason": f"Unique {field} value"
                })
    
    # Check for specific DMBTR and WRBTR ranges (first range)
    if (entry['DMBTR'].values[0] > 910000 and 
        entry['DMBTR'].values[0] < 911000 and 
        entry['WRBTR'].values[0] > 54000 and 
        entry['WRBTR'].values[0] < 55000):
        
        is_anomaly = True
        anomaly_features.append({
            "feature": "DMBTR_WRBTR_RANGE_1",
            "value": f"DMBTR={entry['DMBTR'].values[0]}, WRBTR={entry['WRBTR'].values[0]}",
            "reason": "Values fall in suspicious range (DMBTR: 910000-911000, WRBTR: 54000-55000)"
        })
    
    # Check for specific DMBTR and WRBTR ranges (second range)
    if (entry['DMBTR'].values[0] > 92445000 and 
        entry['DMBTR'].values[0] < 92446000 and 
        entry['WRBTR'].values[0] > 59585000 and 
        entry['WRBTR'].values[0] < 59586000):
        
        is_anomaly = True
        anomaly_features.append({
            "feature": "DMBTR_WRBTR_RANGE_2",
            "value": f"DMBTR={entry['DMBTR'].values[0]}, WRBTR={entry['WRBTR'].values[0]}",
            "reason": "Values fall in suspicious range (DMBTR: 92445000-92446000, WRBTR: 59585000-59586000)"
        })
    
    result = {
        "is_anomaly": is_anomaly,
        "anomaly_features": anomaly_features
    }
    
    if not is_anomaly:
        result["message"] = "No anomalies detected"
    
    return result
