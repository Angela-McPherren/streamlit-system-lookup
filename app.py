import streamlit as st
import pandas as pd

# Load the cleaned configurator data
data = {
    'Application': ['Commercial/Residential', 'Commercial/Residential', 'Commercial/Residential', 'Commercial/Residential', 'Commercial/Residential'],
    'Body Manufacturer': ['McNeilus', 'McNeilus', 'McNeilus', 'McNeilus', 'McNeilus'],
    'Body Model': ['25 yd HD REL, 3.5 yd TG (2516)', '28 yd ZR (2848)', '28 yd ZR (2848)', '36 yd Atlantic (3629)', '40 yd Meridian'],
    'Chassis Manufacturer': ['Peterbilt', 'Mack', 'Peterbilt', 'Mack', 'Mack'],
    'Chassis Model': ['520', 'LR', '520', 'LR', 'MRU'],
    'Chassis Type': ['Rear Load', 'Side Load - Full Automated', 'Side Load - Full Automated', 'Front Load', 'Front Load'],
    'System Type': ['Canopy Mount', 'Tail Mount', 'Roof Mount', 'Tail Mount', 'Tail Mount'],
    'Part Number 1': ['MN39-1632', 'MN39-1632', 'MN39-1632', 'MN39-1632', 'MN39-1632'],
    'Part Number 2': ['MQ36-1764', 'MG36-1600', 'MG36-1601', 'MG36-1600', 'MG36-1600'],
    'Part Number 3': ['MQ36-1706', 'MQ36-1606', 'MQ36-1606', 'MQ36-1606', 'MQ36-1606'],
    'System Cost': [42567.25, 40189.74, 40189.74, 41463.20, 41463.20],
    'FET': [5378.0700, 5602.7688, 5326.7688, 5575.5840, 5575.5840],
    'Install': [2250, 6500, 4200, 5000, 5000]
}

df = pd.DataFrame(data)

# Streamlit title
st.title("CNG Configurator")

# Filters for the app
application_filter = st.selectbox("Select Application", df['Application'].unique())
body_manufacturer_filter = st.selectbox("Select Body Manufacturer", df['Body Manufacturer'].unique())
system_type_filter = st.selectbox("Select System Type", df['System Type'].unique())
chassis_type_filter = st.selectbox("Select Chassis Type", df['Chassis Type'].unique())

# Filtering the data based on user selections
filtered_df = df[
    (df['Application'] == application_filter) & 
    (df['Body Manufacturer'] == body_manufacturer_filter) & 
    (df['System Type'] == system_type_filter) &
    (df['Chassis Type'] == chassis_type_filter)
]

# Display filtered results
if filtered_df.empty:
    st.write("No matching results found.")
else:
    st.write(filtered_df[['Body Model', 'Part Number 1', 'Part Number 2', 'Part Number 3', 'System Cost', 'FET', 'Install']])

# To run the app:
# Save this code in a file called app.py and run it with the command: streamlit run app.py
