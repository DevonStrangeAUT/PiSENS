import argparse
from sense_hat import SenseHat

sense = SenseHat()

def main():
    parser = argparse.ArgumentParser(description='Read Sensor Data from Sense Hat')
    parser.add_argument(
        "Sensor Type",
        choices=[
        "humidity",
        "temperature",
        "temperature_from_humidity",
        "pressure",
        "orientation_radians",
        "orientations_degrees",
        "orientation",
        "compass",
        "compass_raw"
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
        "orientations_degrees": sense.get_orientations_degrees,
        "orientation": sense.get_orientation,
        "compass": sense.get_compass,
        "compass_raw": sense.get_compass_raw,
        "accelerometer": sense.get_accelerometer,
        "accelerometer_raw": sense.get_accelerometer_raw,
    }

    function = sensorFunctions[args.SensorType]
    value = function()

    print(f"{args.sensorType}: readings: {value}")

    if __name__ == "__main__":
        main()