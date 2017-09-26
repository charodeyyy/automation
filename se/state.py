# -*- coding: utf-8 -*

import re
import time
from faker import Faker
from tempmail import TempMail


def get_mail():

    f = Faker()
    tm = TempMail(
        login=f.word(),
        domain=u'@p33.org'
    )
    mail = tm.get_email_address()
    return mail


def get_sms_code(mail):

    tm = TempMail()
    mails = str(tm.get_mailbox(mail.encode()))
    parse_html = re.sub(r'[\',\"]', '', mails)
    for _ in range(10):
        if mails != "{'error': 'There are no emails yet'}":
            break
        time.sleep(1)
    code = re.findall('mail_subject: (\d+)', parse_html)
    if code:
        raise Exception('Mailbox do not have any mail')
    return code
