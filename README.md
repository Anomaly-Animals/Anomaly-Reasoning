# Anomaly-Reasoning

Data Processing and Reasoning for anomaly explanation

## Rules found through decision tree
If HKONT or BSCHL or KTOSL are unique that entry is an anomaly

If data[(data['DMBTR'] > 910000) & (data['DMBTR'] < 911000) & (data['WRBTR'] > 54000) & (data['WRBTR'] < 55000)]

If data[(data['DMBTR'] > 92445000) & (data['DMBTR'] < 92446000) & (data['WRBTR'] > 59585000) & (data['WRBTR'] < 59586000)]


If there are more than 2 decimals after the comma is is an anomaly