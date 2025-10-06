from sense_hat import SenseHat

sense = SenseHat()

# == Environment Readings ==

humidity = sense.get_humidity()
temperature = sense.get_temperature()
tempfromHumidity = sense.get_temperature_from_humidity()
pressure = sense.get_pressure()

# == Orientation Readings ==
radians = sense.get_orientation_radians()
degrees = sense.get_orientation_degrees()
orientation = sense.get_orientation()
compass = sense.get_compass()
rawCompass = sense.get_compass_raw()

# == Accelerometer Readings ==

accelerometer = sense.get_accelerometer()
rawAccelerometer = sense.get_accelerometer_raw()


