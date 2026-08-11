import pandas as pd

# Load the sensor data
data = pd.read_csv("data/sensor_data.csv")

# Display the first 5 readings
print("\nFIRST 5 READINGS")
print("----------------")
print(data.head())

# Basic information
print("\nDATASET INFORMATION")
print("-------------------")
print(f"Total readings: {len(data)}")

# Temperature analysis
print("\nTEMPERATURE ANALYSIS")
print("--------------------")
print(f"Average temperature: {data['Temperature'].mean():.2f} °C")
print(f"Maximum temperature: {data['Temperature'].max():.2f} °C")
print(f"Minimum temperature: {data['Temperature'].min():.2f} °C")

# Pressure analysis
print("\nPRESSURE ANALYSIS")
print("-----------------")
print(f"Average pressure: {data['Pressure'].mean():.2f} bar")
print(f"Maximum pressure: {data['Pressure'].max():.2f} bar")

# Vibration analysis
print("\nVIBRATION ANALYSIS")
print("------------------")
print(f"Average vibration: {data['Vibration'].mean():.2f} mm/s")
print(f"Maximum vibration: {data['Vibration'].max():.2f} mm/s")

# RPM analysis
print("\nRPM ANALYSIS")
print("------------")
print(f"Average RPM: {data['RPM'].mean():.0f}")
print(f"Maximum RPM: {data['RPM'].max()}")

# Current analysis
print("\nCURRENT ANALYSIS")
print("----------------")
print(f"Average current: {data['Current'].mean():.2f} A")
print(f"Maximum current: {data['Current'].max():.2f} A")

# Machine status
print("\nMACHINE STATUS")
print("--------------")
print(data["Machine_Status"].value_counts())