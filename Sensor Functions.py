from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()

temperature = sense.get_temperature()

tempfromHumidity = sense.get_temperature_from_humidity()

pressure = sense.get_pressure()

radians = sense.get_orientation_radians()

degrees = sense.get_orientation_degrees()




