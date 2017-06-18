import config
from notifier import EmailNotifier

print(type(config.needNotification))

sender = 'oleg.kaliuzhny@gmail.com'
passw = 'oleh55Softeip'

notif = EmailNotifier(sender, sender, passw)

EmailNotifier.tryLogin(sender, passw)
notif.notify(30, 30, "10:10")
