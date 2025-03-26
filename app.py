import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@st.cache_data
def load_data():
    return pd.read_excel("system_lookup.xlsx")

df = load_data()
st.title("🔍 System PN Lookup")

# Step-by-step dropdowns with filtered options
application = st.selectbox("Application", sorted(df["Application"].unique()))
df_filtered = df[df["Application"] == application]

cng_mounting = st.selectbox("CNG Mounting", sorted(df_filtered["CNG MOUNTING"].unique()))
df_filtered = df_filtered[df_filtered["CNG MOUNTING"] == cng_mounting]

body_mfg = st.selectbox("Body MFG", sorted(df_filtered["Body MFG"].unique()))
df_filtered = df_filtered[df_filtered["Body MFG"] == body_mfg]

body_details = st.selectbox("Body MFG Details", sorted(df_filtered["Body MFG Details"].unique()))
df_filtered = df_filtered[df_filtered["Body MFG Details"] == body_details]

chassis_mfg = st.selectbox("Chassis MFG", sorted(df_filtered["Chassis MFG"].unique()))
df_filtered = df_filtered[df_filtered["Chassis MFG"] == chassis_mfg]

chassis_model = st.selectbox("Chassis Model", sorted(df_filtered["Chassis Model"].unique()))
df_filtered = df_filtered[df_filtered["Chassis Model"] == chassis_model]

chassy = st.selectbox("Chassy", sorted(df_filtered["Chassy"].unique()))
df_filtered = df_filtered[df_filtered["Chassy"] == chassy]

chassis_type = st.selectbox("Chassis Type", sorted(df_filtered["Chassis Type"].unique()))
df_filtered = df_filtered[df_filtered["Chassis Type"] == chassis_type]

system_type = st.selectbox("System Type", sorted(df_filtered["System Type"].unique()))
df_filtered = df_filtered[df_filtered["System Type"] == system_type]

system_dge = st.selectbox("System DGE", sorted(df_filtered["System DGE"].unique()))
df_filtered = df_filtered[df_filtered["System DGE"] == system_dge]

# Result
if not df_filtered.empty:
    st.success("🎯 Match Found!")
    system_pn = df_filtered.iloc[0]["SYSTEM PN"]
    second_pn = df_filtered.iloc[0]["2nd System PN"]

    st.write("**System PN:**", system_pn)
    st.write("**2nd System PN:**", second_pn)

    # Create PDF in memory
    def generate_pdf():
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        y = height - 50
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "System PN Lookup Report")

        c.setFont("Helvetica", 12)
        y -= 30
        c.drawString(50, y, f"Application: {application}")
        y -= 20
        c.drawString(50, y, f"CNG Mounting: {cng_mounting}")
        y -= 20
        c.drawString(50, y, f"Body MFG: {body_mfg}")
        y -= 20
        c.drawString(50, y, f"Body MFG Details: {body_details}")
        y -= 20
        c.drawString(50, y, f"Chassis MFG: {chassis_mfg}")
        y -= 20
        c.drawString(50, y, f"Chassis Model: {chassis_model}")
        y -= 20
        c.drawString(50, y, f"Chassy: {chassy}")
        y -= 20
        c.drawString(50, y, f"Chassis Type: {chassis_type}")
        y -= 20
        c.drawString(50, y, f"System Type: {system_type}")
        y -= 20
        c.drawString(50, y, f"System DGE: {system_dge}")
        y -= 30
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, f"System PN: {system_pn}")
        y -= 20
        c.drawString(50, y, f"2nd System PN: {second_pn}")

        c.save()
        buffer.seek(0)
        return buffer

    pdf_file = generate_pdf()

    st.download_button(
        label="📄 Download PDF",
        data=pdf_file,
        file_name="system_pn_lookup.pdf",
        mime="application/pdf"
    )
else:
    st.warning("No matching configuration found.")
