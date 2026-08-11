# Industrial IoT Monitoring System with AI Anomaly Detection

## 📌 Project Overview

This project is an **Industrial IoT monitoring system** designed to simulate, analyze, visualize, and monitor industrial machine sensor data.

The system combines **traditional rule-based monitoring** with **Machine Learning-based anomaly detection** to identify unusual machine behavior and estimate maintenance risk through an interactive **Streamlit dashboard**.

The system simulates industrial machine parameters such as temperature, pressure, vibration, RPM, and electrical current.

---

## 🎯 Project Objectives

* Simulate industrial machine sensor data
* Store sensor readings in CSV format
* Analyze sensor data using Python
* Visualize machine parameters
* Detect abnormal machine behavior using Machine Learning
* Compare rule-based monitoring with AI anomaly detection
* Calculate anomaly scores
* Classify maintenance risk
* Display results using an interactive dashboard

---

## 🏭 Sensors Monitored

The system monitors five major industrial parameters:

* 🌡️ Temperature
* 📊 Pressure
* 📳 Vibration
* ⚙️ RPM
* ⚡ Current

---

## 🏗️ System Architecture

```text
Industrial Sensor Simulation
            ↓
      Sensor Data CSV
            ↓
       Data Analysis
            ↓
     Rule-Based Monitoring
            ↓
    AI Feature Extraction
            ↓
      Isolation Forest
            ↓
     Anomaly Detection
            ↓
       Anomaly Score
            ↓
     Maintenance Risk
            ↓
    Streamlit Dashboard
```

---

## 🤖 AI Anomaly Detection

The system uses **Machine Learning-based anomaly detection** to identify unusual combinations of industrial sensor values.

The AI pipeline includes:

1. Loading sensor data
2. Selecting relevant sensor features
3. Preparing the feature matrix
4. Training the anomaly detection model
5. Generating anomaly predictions
6. Calculating anomaly scores
7. Comparing AI results with rule-based machine status
8. Estimating maintenance risk

### Machine Learning Model

The project uses the **Isolation Forest** algorithm for unsupervised anomaly detection.

Isolation Forest is suitable for industrial monitoring because it can identify unusual observations without requiring manually labelled fault data.

### AI Features

```text
Temperature
Pressure
Vibration
RPM
Current
```

---

## ⚙️ Rule-Based Monitoring

In addition to AI-based detection, the system uses predefined operating limits to identify potentially abnormal machine conditions.

Sensor readings are evaluated against defined thresholds and the machine is classified into different operating conditions such as:

```text
NORMAL
WARNING
```

The rule-based results are then compared with the AI anomaly detection results.

---

## 📊 Anomaly Score

The Machine Learning model generates anomaly information that is used to determine how unusual a machine's sensor combination is.

The anomaly information is combined with the machine's operating status to support maintenance-risk estimation.

---

## 🛠️ Maintenance Risk Estimation

The system estimates machine maintenance risk using sensor conditions and anomaly detection results.

The purpose is to provide an early indication of potentially abnormal machine behavior and help identify machines that may require further inspection.

---

## 📈 Streamlit Dashboard

An interactive **Streamlit dashboard** is used to visualize the monitoring results.

The dashboard provides:

* Real-time-style sensor visualization
* Temperature monitoring
* Pressure monitoring
* Vibration monitoring
* RPM monitoring
* Current monitoring
* Machine operating status
* AI anomaly detection results
* Anomaly information
* Maintenance-risk indication

---

## 💻 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Streamlit**
* **Git & GitHub**
* **Machine Learning**
* **Industrial IoT concepts**

---

## 📁 Project Structure

```text
Industrial-IOT-Monitoring/
│
├── sensor_simulator.py
├── visualize_data.py
├── README.md
├── sensor_data.csv
└── dashboard/
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project

```bash
cd Industrial-IOT-Monitoring
```

### 3. Install the required Python packages

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

### 4. Run the sensor simulator

```bash
python sensor_simulator.py
```

### 5. Run the Streamlit dashboard

```bash
streamlit run visualize_data.py
```

The dashboard will open in your browser.

---

## 🔍 Project Workflow

```text
Sensor Simulation
       ↓
Sensor Data Generation
       ↓
CSV Data Storage
       ↓
Data Analysis
       ↓
Rule-Based Machine Monitoring
       ↓
Machine Learning
       ↓
Anomaly Detection
       ↓
Anomaly Score
       ↓
Maintenance Risk
       ↓
Streamlit Visualization
```

---

## 🚀 Future Improvements

Potential future improvements include:

* Integration with real industrial sensors
* IoT cloud connectivity
* Real-time sensor streaming
* Automated maintenance alerts
* Predictive maintenance using time-series data
* Edge AI deployment
* Industrial communication protocols
* Database integration
* Advanced machine-learning models

---

## 👩‍💻 Project Focus

This project demonstrates the integration of:

**Industrial IoT + Python + Machine Learning + Data Visualization + AI-based Anomaly Detection**

The project is designed as a practical foundation for developing intelligent industrial monitoring and predictive maintenance systems.
