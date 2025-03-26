import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_excel("system_lookup.xlsx")
    return df

df = load_data()

st.title("System PN Lookup App")

# Input fields
application = st.selectbox("Application", df["Application"].unique())
cng_mounting = st.selectbox("CNG Mounting", df["CNG MOUNTING"].unique())
body_mfg = st.selectbox("Body MFG", df["Body MFG"].unique())
body_mfg_details = st.selectbox("Body MFG Details", df["Body MFG Details"].unique())
chassis_mfg = st.selectbox("Chassis MFG", df["Chassis MFG"].unique())
chassis_model = st.selectbox("Chassis Model", df["Chassis Model"].unique())
chassy = st.selectbox("Chassy", df["Chassy"].unique())
chassis_type = st.selectbox("Chassis Type", df["Chassis Type"].unique())
system_type = st.selectbox("System Type", df["System Type"].unique())
system_dge = st.selectbox("System DGE", df["System DGE"].unique())

# Filter the DataFrame
filtered = df[
    (df["Application"] == application) &
    (df["CNG MOUNTING"] == cng_mounting) &
    (df["Body MFG"] == body_mfg) &
    (df["Body MFG Details"] == body_mfg_details) &
    (df["Chassis MFG"] == chassis_mfg) &
    (df["Chassis Model"] == chassis_model) &
    (df["Chassy"] == chassy) &
    (df["Chassis Type"] == chassis_type) &
    (df["System Type"] == system_type) &
    (df["System DGE"] == system_dge)
]

if not filtered.empty:
    st.success("Match found!")
    st.write("**System PN:**", filtered.iloc[0]["SYSTEM PN"])
    st.write("**2nd System PN:**", filtered.iloc[0]["2nd System PN"])
else:
    st.warning("No matching entry found.")
