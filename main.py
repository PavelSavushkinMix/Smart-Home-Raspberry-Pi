import dht22
import datetime
from notifier import EmailNotifier
from displayILI import DisplayTFT144
from time import sleep
import config

#config
needNotification = False
sendEachHours = 3
notifyOnEmail = ''
passwordEmail = ''
displayEnabled = False
updateEachMinutes = 0.25
recieverName = ''
#

if type(config.needNotification) is bool:
	needNotification = config.needNotification
else:
	print("needNotification - Fail to load value")

if type(config.sendEachHours) is int and 0 < config.sendEachHours < 60:
	sendEachHours = config.sendEachHours
else:
	print("sendEachHours - Fail to load value")

if type(config.passwordEmail) is str:
	passwordEmail = config.passwordEmail
else:
	print("passwordEmail - Fail to load value")

if type(config.displayEnabled) is bool:
	displayEnabled = config.displayEnabled
else:
	print("displayEnabled - Fail to load value")

if type(config.updateEachMinutes) is float:
	updateEachMinutes = config.updateEachMinutes
else:
	print("updateEachMinutes - Fail to load value")

if type(config.notifyOnEmail) is str:
	notifyOnEmail = config.notifyOnEmail
	if EmailNotifier.tryLogin(notifyOnEmail, passwordEmail) == 1:
		needNotification = False
else:
	print("notifyOnEmail - Failed to load value")

if type(config.recieverName) is str:
	recieverName = config.recieverName
else:
	print("recieverName - Fail to load value")

if displayEnabled:
	display = DisplayTFT144()

notifier = EmailNotifier(notifyOnEmail, notifyOnEmail, passwordEmail)
humidity, temperature = 0.0, 0.0

#Update 
lastHour = datetime.datetime.now().hour - sendEachHours #for notifier
lastMin = datetime.datetime.now().minute - updateEachMinutes  #for sensor
#

while True:
	now = datetime.datetime.now()

	if (lastMin*60 + updateEachMinutes*60) % 3600 <= datetime.datetime.now().minute*60:
		humidity, temperature = dht22.readFromDHT()
		if humidity is None:
			humidity = 0.0
		if temperature is None:	
			temperature = 0.0
		if displayEnabled:
			display.printData(temperature, humidity, now)
		else:
			print("Temp: {0}, Hum: {1}, Time: {2}".format(temperature, humidity, now))
		lastMin = datetime.datetime.now().minute

	if (lastHour + sendEachHours) % 24 == datetime.datetime.now().hour:
		lastHour = datetime.datetime.now().hour
		now = "{0}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}".format(now.year, now.month, now.day, now.hour, now. minute, now.second)
		if needNotification:
			notifier.notify(temperature, humidity, now, recieverName=recieverName)
	sleep(3)
		
