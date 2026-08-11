# Industrial IoT Monitoring System

## 📌 Project Overview

An Industrial IoT monitoring system developed to simulate machine sensor data, monitor machine health, detect abnormal operating conditions using AI, and estimate maintenance risk through an interactive Streamlit dashboard.

The project combines sensor simulation, rule-based monitoring, machine-learning anomaly detection, data analysis, and real-time visualization.

---

## 🎯 Objectives

- Simulate industrial machine sensor readings
- Monitor machine operating conditions
- Detect abnormal sensor behavior
- Compare rule-based monitoring with AI-based anomaly detection
- Estimate machine maintenance risk
- Visualize machine health through an interactive dashboard

---

## 🏭 Sensors Monitored

The system monitors five major industrial parameters:

- 🌡️ Temperature
- 📊 Pressure
- 📳 Vibration
- ⚙️ RPM
- ⚡ Current

---

## 🤖 AI Anomaly Detection

The system uses machine-learning based anomaly detection to identify unusual combinations of sensor values.

The AI pipeline includes:

1. Loading sensor data
2. Selecting relevant sensor features
3. Preparing the feature matrix
4. Training the anomaly detection model
5. Generating anomaly predictions
6. Calculating anomaly scores
7. Comparing AI results with rule-based machine status

### AI Features

```text
Temperature
Pressure
Vibration
RPM
Current