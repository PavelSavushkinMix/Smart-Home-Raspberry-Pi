import Adafruit_DHT

def readFromDHT():
	return Adafruit_DHT.read_retry(22, 17)

