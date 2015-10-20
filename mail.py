
import sys
from email.mime.text import MIMEText
from datetime import date
import smtplib

from mailAuth import *
'''
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "...@gmail.com"
SMTP_PASSWORD = ""
EMAIL_FROM = SMTP_USERNAME
'''

EMAIL_TO = []
EMAIL_SUBJECT = None

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

def sendMail(subj, body, frm=EMAIL_FROM, to=EMAIL_TO):
  msg = MIMEText(body)
  msg['Subject'] = subj
  msg['To'] = EMAIL_SPACE.join(to)
  msg['From'] = frm
  mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
  mail.starttls()
  mail.login(SMTP_USERNAME, SMTP_PASSWORD)
  mail.sendmail(frm, to, msg.as_string())
  mail.quit()

def main(msg):
  sendMail('', msg)

if __name__ == '__main__':
  msg = 'Email from python'
  if len(sys.argv) > 1:
    msg = sys.argv[1]
  main(msg)

