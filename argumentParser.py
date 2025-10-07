import argparse
import sqlite3
import os
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

DB_FILE = os.path.join(os.getcwd(), "sensor_readings.db")

def save_readings(SensorType, value):
    """Save a sensor reading to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # If a table doesn't exist within the db, make one.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_type TEXT NOT NULL,
            value TEXT NOT NULL,
            timestamp DATETIME NOT NULL
        )
    """)

    # Insert the new reading
    cursor.execute(
        "INSERT INTO readings (sensor_type, value, timestamp) VALUES (?, ?, ?)",
        (SensorType, str(value), datetime.now())
    )

    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Read Sensor Data from Sense Hat.')
    parser.add_argument(
        "SensorType",
        choices=[
        "humidity",
        "temperature",
        "temperature_from_humidity",
        "pressure",
        "orientation_radians",
        "orientation_degrees",
        "orientation",
        "compass",
        "compass_raw",
        "accelerometer",
        "accelerometer_raw",
    ],
        help="Type of sensor to read",
    )

    args = parser.parse_args()

    sensorFunctions = {
        "humidity": sense.get_humidity,
        "temperature": sense.get_temperature,
        "temperature_from_humidity": sense.get_temperature_from_humidity,
        "pressure": sense.get_pressure,
        "orientation_radians": sense.get_orientation_radians,
        "orientation_degrees": sense.get_orientation_degrees,
        "orientation": sense.get_orientation,
        "compass": sense.get_compass,
        "compass_raw": sense.get_compass_raw,
        "accelerometer": sense.get_accelerometer,
        "accelerometer_raw": sense.get_accelerometer_raw,
    }

    function = sensorFunctions[args.SensorType]
    value = function()

    if isinstance(value, (int, float)):
        print(f"{value:.2f}")
    else:
        print(value)

# == Local SQLite Functionality ==

    # Save to SQLite
    save_readings(args.SensorType, value)

if __name__ == "__main__":
    main()