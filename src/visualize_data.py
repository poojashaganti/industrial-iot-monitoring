import pandas as pd
import matplotlib.pyplot as plt

# Load sensor data
data = pd.read_csv("data/sensor_data.csv")

# Convert timestamp
data["Timestamp"] = pd.to_datetime(data["Timestamp"])

# -----------------------------
# Temperature
# -----------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["Timestamp"],
    data["Temperature"],
    label="Temperature"
)

plt.axhline(
    y=75,
    linestyle="--",
    label="Warning Limit (75°C)"
)

plt.title("Industrial Machine Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# Pressure
# -----------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["Timestamp"],
    data["Pressure"],
    label="Pressure"
)

plt.axhline(
    y=5.5,
    linestyle="--",
    label="Warning Limit (5.5 bar)"
)

plt.title("Industrial Machine Pressure")
plt.xlabel("Time")
plt.ylabel("Pressure (bar)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# Vibration
# -----------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["Timestamp"],
    data["Vibration"],
    label="Vibration"
)

plt.axhline(
    y=4,
    linestyle="--",
    label="Warning Limit (4 mm/s)"
)

plt.title("Industrial Machine Vibration")
plt.xlabel("Time")
plt.ylabel("Vibration (mm/s)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# RPM
# -----------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["Timestamp"],
    data["RPM"],
    label="RPM"
)

plt.title("Industrial Machine RPM")
plt.xlabel("Time")
plt.ylabel("RPM")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# Current
# -----------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    data["Timestamp"],
    data["Current"],
    label="Current"
)

plt.axhline(
    y=15,
    linestyle="--",
    label="Warning Limit (15 A)"
)

plt.title("Industrial Machine Current")
plt.xlabel("Time")
plt.ylabel("Current (A)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()