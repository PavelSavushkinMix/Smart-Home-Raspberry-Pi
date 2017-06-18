from smartGPIO import GPIO
from lib_tft144 import TFT144
import sys
import datetime

class DisplayTFT144:
	#TFT = None
	
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		RST = 25    # RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
		CE =   0    # RPI GPIO: 0 or 1 for CE0 / CE1 number (NOT the pin#)
		DC =  24    # Labeled on board as "A0"   Command/Data select
		LED = 0    # LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V

		import spidev
		spi = spidev.SpiDev()

		print ("Starting TFT...")
		self.TFT = TFT144(GPIO, spi, CE, DC, RST, LED, TFT144.ORIENTATION0, isRedBoard=False, spi_speed=32000000)

	

	def printData(self, temperature, humidity, time):
		tempColor = self.TFT.colour565(110, 188, 0)
		humColor = self.TFT.colour565(110, 188, 0)
		try:
			if temperature <= 25:
				tempColor = self.TFT.colour565(71, 114, 255)
			elif temperature > 28 and temperature < 30:
				tempColor = self.TFT.colour565(255, 131, 0)
			elif temperature > 30:
				tempColor = self.TFT.RED
			else:
				tempColor = self.TFT.colour565(110, 188, 0)

			if humidity < 40 or humidity > 60:
				humColor = self.TFT.RED
			else:
				humColor = self.TFT.colour565(110,188,0)
	
		except:
			temperature = -1
			humidity = -1
			tempColor = self.TFT.RED
			humColor = self.TFT.RED
		
		self.TFT.put_string("T: {0:2.1f} *C".format(temperature), 0, 0, tempColor, self.TFT.BLACK, 4)
		self.TFT.put_string("H: {0:2.1f}  %".format(humidity), 0, 20, humColor, self.TFT.BLACK, 4)
		self.TFT.put_string("{0:02}:{1:02}".format(time.hour, time.minute), 0, 90, self.TFT.WHITE, self.TFT.BLACK, 8)
