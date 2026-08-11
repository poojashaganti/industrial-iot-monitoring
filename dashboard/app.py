import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, key="dashboard_refresh")

# Page configuration
st.set_page_config(
    page_title="Industrial IoT Monitoring",
    page_icon="⚙️",
    layout="wide"
)

# Load sensor data
data = pd.read_csv("data/sensor_data.csv")

# Convert timestamp
data["Timestamp"] = pd.to_datetime(data["Timestamp"])

# Title
st.title("⚙️ Industrial IoT Monitoring System")
st.write("Real-time machine sensor monitoring and analysis")

# Latest reading
latest = data.iloc[-1]

# Machine status
status = latest["Machine_Status"]

if status == "WARNING":
    st.error("⚠️ MACHINE STATUS: WARNING")
else:
    st.success("✅ MACHINE STATUS: NORMAL")

# Sensor values
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🌡️ Temperature",
        f"{latest['Temperature']:.2f} °C"
    )

with col2:
    st.metric(
        "💨 Pressure",
        f"{latest['Pressure']:.2f} bar"
    )

with col3:
    st.metric(
        "📳 Vibration",
        f"{latest['Vibration']:.2f} mm/s"
    )

with col4:
    st.metric(
        "⚙️ RPM",
        f"{latest['RPM']}"
    )

with col5:
    st.metric(
        "🔌 Current",
        f"{latest['Current']:.2f} A"
    )

# Temperature chart
st.subheader("🌡️ Temperature Trend")

st.line_chart(
    data.set_index("Timestamp")["Temperature"]
)

# Pressure chart
st.subheader("💨 Pressure Trend")

st.line_chart(
    data.set_index("Timestamp")["Pressure"]
)

# Vibration chart
st.subheader("📳 Vibration Trend")

st.line_chart(
    data.set_index("Timestamp")["Vibration"]
)

# Recent readings
st.subheader("📊 Recent Sensor Readings")

st.dataframe(
    data.tail(10),
    use_container_width=True
)
# AI MACHINE HEALTH
st.subheader("🤖 AI Machine Health")

ai_data = pd.read_csv("data/ai_sensor_results.csv")

latest_ai = ai_data.iloc[-1]

ai_status = latest_ai["AI_Anomaly"]
anomaly_score = latest_ai["Anomaly_Score"]
maintenance_risk = latest_ai["Maintenance_Risk"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "AI Anomaly Status",
        ai_status
    )

with col2:
    st.metric(
        "Anomaly Score",
        round(anomaly_score, 4)
    )

with col3:
    st.metric(
        "Maintenance Risk",
        maintenance_risk
    )
# AI Anomaly Score Trend
st.subheader("📈 AI Anomaly Score Trend")

st.line_chart(
    ai_data.set_index("Timestamp")["Anomaly_Score"]
)    
# Maintenance Risk Distribution
st.subheader("🛠️ Maintenance Risk Distribution")

risk_counts = ai_data["Maintenance_Risk"].value_counts()

st.bar_chart(risk_counts)
# AI Summary
st.subheader("📋 AI Monitoring Summary")

total_readings = len(ai_data)
total_anomalies = (ai_data["AI_Anomaly"] == "ANOMALY").sum()
total_high_risk = (ai_data["Maintenance_Risk"] == "HIGH").sum()

st.write("Total readings analyzed:", total_readings)
st.write("AI anomalies detected:", total_anomalies)
st.write("High-risk readings:", total_high_risk)