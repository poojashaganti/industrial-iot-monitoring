import pandas as pd
from sklearn.ensemble import IsolationForest

# Load sensor data
data = pd.read_csv("data/sensor_data.csv")

print("Total sensor readings:", len(data))
print("\nSensor data:")
print(data.head())

# Select sensor features for the AI model
features = [
    "Temperature",
    "Pressure",
    "Vibration",
    "RPM",
    "Current"
]

X = data[features]

print("\nAI FEATURES:")
print(X.head())

print("\nFeature shape:", X.shape)

# Create the Isolation Forest model
model = IsolationForest(
    contamination=0.10,
    random_state=42
)

# Train the model
model.fit(X)

print("\nAI MODEL TRAINING COMPLETE!")
# Predict anomalies
predictions = model.predict(X)

# Convert predictions into readable labels
data["AI_Anomaly"] = predictions

data["AI_Anomaly"] = data["AI_Anomaly"].map({
    1: "NORMAL",
    -1: "ANOMALY"
})

print("\nAI ANOMALY RESULTS:")
print(data["AI_Anomaly"].value_counts())
# Compare rule-based status with AI results
comparison = pd.crosstab(
    data["Machine_Status"],
    data["AI_Anomaly"]
)

print("\nRULE-BASED vs AI COMPARISON:")
print(comparison)
# Calculate anomaly scores
data["Anomaly_Score"] = model.decision_function(X)

print("\nMOST UNUSUAL READINGS:")
print(
    data[
        [
            "Timestamp",
            "Temperature",
            "Pressure",
            "Vibration",
            "RPM",
            "Current",
            "Machine_Status",
            "AI_Anomaly",
            "Anomaly_Score"
        ]
    ]
    .sort_values("Anomaly_Score")
    .head(10)
)
# Create maintenance risk levels
def maintenance_risk(row):
    if row["AI_Anomaly"] == "ANOMALY":
        if row["Anomaly_Score"] < -0.06:
            return "HIGH"
        else:
            return "MEDIUM"
    else:
        return "LOW"


data["Maintenance_Risk"] = data.apply(maintenance_risk, axis=1)

print("\nMAINTENANCE RISK:")
print(data["Maintenance_Risk"].value_counts())
# Save AI results
output_file = "data/ai_sensor_results.csv"

data.to_csv(output_file, index=False)

print("\nAI RESULTS SAVED!")
print("File:", output_file)