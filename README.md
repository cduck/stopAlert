
###To use
Enter your email account login credentials in mailAuth.py.  This program will
log into this email account to send the alert emails.

Modify the list of email addresses in alertConfig.py and optionally configure the other settings.

####Run using python 2

$ python alertConfig.py

####If running on a linux server from a startup script

nohup sudo -u <username> /usr/bin/python /path/to/stopAlert.py >/tmp/stopAlertLog 2>&1 &

