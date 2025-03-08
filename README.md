# Anomaly-Reasoning

Data Processing and Reasoning for anomaly explanation

## Rules found through decision tree
If HKONT or BSCHL or KTOSL are unique that entry is an anomaly

If data[(data['DMBTR'] > 910000) & (data['DMBTR'] < 911000) & (data['WRBTR'] > 54000) & (data['WRBTR'] < 55000)]

If data[(data['DMBTR'] > 92445000) & (data['DMBTR'] < 92446000) & (data['WRBTR'] > 59585000) & (data['WRBTR'] < 59586000)]


If there are more than 2 decimals after the comma is is an anomaly

## Start the Backend
- Make sure you have flask and other necessary packages installed via `poetry install`. 
- Run the command `make run-backend` to start the server

## Make requests to the backend
- You can make requests to the endpoint `http://127.0.0.1:5000/reasoning-for-anomaly`
- The request body needs to look like this:
```json
{
 "anomaly_belnr": 507636
}
```