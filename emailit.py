#!/usr/bin/env python3
import sys
import smtplib
from email.mime.text import MIMEText

emailusername = 'my@email.com'
emailpassword = 'EXAMPLE PASSWORD 999'
myemailaddr = 'my@email.com'
toemailaddr = ['demo@alert.com', 'example@vtext.com']
smtphost = 'mail.email.com'
smtpport = 465


def emailMsg(u, p, subject, message):
    msg = MIMEText(message)
    msg['From'] = myemailaddr

    msg['Subject'] = subject
    emaillist = toemailaddr
    msg['To'] = emaillist[0]
    msg['Cc'] = ','.join(emaillist[1:])

    try:
        server = smtplib.SMTP_SSL(smtphost, smtpport)        
        server.login(u, p)
        server.sendmail(myemailaddr, emaillist, msg.as_string())
        server.quit()
    except SMTPAuthenticationError as e:
        print("SMTP login failed %s" % e);
    except SMTPException as e:
        print("SMTP send failed %s" % e);


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('%s message...' % sys.argv[0])
    else:
        emailMsg(emailusername, emailpassword, sys.argv[1], ' '.join(sys.argv[1:]))
