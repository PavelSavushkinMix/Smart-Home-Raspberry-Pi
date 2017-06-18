import smtplib
import datetime

class EmailNotifier:
	sender = ''
	recievers = ['']
	password = ""
	
	def __init__(self, sender, reciever, password):
		self.sender = sender
		self.recievers = [reciever]
		self.password = password

	def tryLogin(login, password):
		try:
			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.starttls()
			smtpObj.login(login, password)
			smtpObj.quit()
			print ("Successfully logged in (e-mail)")
			return 0
		except Exception:
			print ("Error: unable to log in (e-mail)")
			return 1

	def notify(self, temperature, humidity, time, title='Smart Home Info', warningText='', senderName='Smart Home Raspberry Pi 3', recieverName=''):
		message = """From: {5} <{7}>
To: {6} <{7}>
Subject: {3}

{4}

Temperature: {0:0.1f} *C
Humidity: {1:0.1f} %
Time: {2}
""".format(temperature, humidity, time, title, warningText, senderName, recieverName, self.recievers[0])

		
		
		try:
			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.starttls()
			smtpObj.login(self.sender, self.password)
			smtpObj.sendmail(self.sender, self.recievers, message)
			smtpObj.quit()
			print ("Successfully sent email")
		except Exception:
			print ("Error: unable to send email")
