import smtplib
from email.mime.text import MIMEText
from sms import PROVIDERS
username = "egclearance@gmail.com"
password = "fcormefybepkdoet"

vtext = "251902229324@vtext.com"
message = "this is the message to be sent"

msg = MIMEText("""From: %s
To: %s
Subject: text-message
%s""" % (username, vtext, message))

server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
server.login(username,password)
server.sendmail(username, vtext, msg.as_string())
server.quit()