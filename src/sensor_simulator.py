import random
import time
import csv
from datetime import datetime

# Create/open the CSV file
file = open("data/sensor_data.csv", "a", newline="")

writer = csv.writer(file)

# Add column names if the file is empty
if file.tell() == 0:
    writer.writerow([
        "Timestamp",
        "Temperature",
        "Pressure",
        "Vibration",
        "RPM",
        "Current",
        "Machine_Status"
    ])

print("Industrial IoT Monitoring System")
print("Data logging started...")
print("Press Ctrl+C to stop")
print("--------------------------------")

try:

    while True:

        # Simulated industrial sensors
        temperature = random.uniform(40, 90)
        pressure = random.uniform(2, 6)
        vibration = random.uniform(0.5, 4)
        rpm = random.randint(1000, 1800)
        current = random.uniform(5, 15)

        # Check sensor conditions
        temperature_status = "HIGH" if temperature > 75 else "NORMAL"
        pressure_status = "HIGH" if pressure > 5.5 else "NORMAL"
        vibration_status = "HIGH" if vibration > 4 else "NORMAL"
        rpm_status = "HIGH" if rpm > 1800 else "NORMAL"
        current_status = "HIGH" if current > 15 else "NORMAL"

        # Overall machine status
        if "HIGH" in [
            temperature_status,
            pressure_status,
            vibration_status,
            rpm_status,
            current_status
        ]:
            machine_status = "WARNING"
        else:
            machine_status = "NORMAL"

        # Current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save data
        writer.writerow([
            timestamp,
            round(temperature, 2),
            round(pressure, 2),
            round(vibration, 2),
            rpm,
            round(current, 2),
            machine_status
        ])

        # Make sure data is saved immediately
        file.flush()

        # Display readings
        print(f"{timestamp}")
        print(f"Temperature : {temperature:.2f} °C  {temperature_status}")
        print(f"Pressure    : {pressure:.2f} bar  {pressure_status}")
        print(f"Vibration   : {vibration:.2f} mm/s  {vibration_status}")
        print(f"RPM         : {rpm}  {rpm_status}")
        print(f"Current     : {current:.2f} A  {current_status}")
        print(f"Machine Status: {machine_status}")
        print("--------------------------------")

        time.sleep(1)

except KeyboardInterrupt:

    print("\nData logging stopped.")

finally:

    file.close()