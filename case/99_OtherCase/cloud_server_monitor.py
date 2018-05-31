# -*- encoding: utf-8 -*-

import poplib
from twilio.rest import Client
from email.parser import Parser
from datetime import datetime
from datetime import timedelta
from time import sleep

VAR_SUBJECT = "Verification code"  # mail subject
VAR_SMSCONTENT = "can't receive email in one hour"  # sms content
VAR_SMS_NUMBER = '+8615989303854'

TWILIO_ACCOUNT = 'AC573b93f3a0b29d4ac179cfccf247b244'
TWILIO_TOKEN = '06466eee339b9b4fcd27e673348f6ecf'
TWILIO_PHONE = '+18162031364'

email_send = 'smtp.exmail.qq.com'
email_receive = 'pop.exmail.qq.com'
email_username = 'valmk20@alcatel-move.com'
email_password = 'zt3Gy3|MT('
email_address = "https://exmail.qq.com"


def send_sms(text=VAR_SMSCONTENT):
    client = Client(TWILIO_ACCOUNT, TWILIO_TOKEN)
    message = client.messages.create(to=VAR_SMS_NUMBER, from_=TWILIO_PHONE, body=text)
    print(message.sid)


def get_latest_email():
    current_time = datetime.now()
    server = poplib.POP3_SSL(email_receive)
    server.user(email_username)
    server.pass_(email_password)
    print('Messages: %s, Size: %s' % server.stat())
    resp_one, mails, octets_one = server.list()
    # print(mails)
    index = len(mails)
    resp_two, lines, octets_two = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # print(msg_content)
    msg = Parser().parsestr(msg_content)
    mail_from = msg.get('From', '')
    mail_to = msg.get('To', '')
    mail_subject = msg.get('Subject', '')
    # mail_date = msg.get('Date', '')
    mail_date = datetime.strptime(msg.get('Date'), '%a, %d %b %Y %H:%M:%S +0000 (UTC)')
    mail_local_time = mail_date + timedelta(hours=+8)
    print("From: %s" % mail_from)
    print("To: %s" % mail_to)
    print("Subject: %s " % mail_subject)
    print("Date: %s" % mail_local_time)
    server.quit()
    interval = (current_time - mail_local_time).seconds
    print("interval:%s" % interval)
    if str(mail_subject).__contains__(VAR_SUBJECT) and interval < 4500:
        return True

    return False


def output(text):
    print("\r%4s" % text, end='')


def waiting(time):
    for i in range(time):
        output(i)
        sleep(1)


if __name__ == '__main__':
    while True:
        try:
            if get_latest_email() is False:
                print('send message')
                send_sms()
        except BaseException:
            continue
        waiting(3600)
        print("")
    # send_sms()
