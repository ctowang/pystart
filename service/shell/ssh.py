# -*- coding: utf-8 -*-

import paramiko
import sys
import getpass
import threading
import os
host = "153.35.93.117"
port = 22
user = "root"
password = "6yhn^YHN"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect(host,username=user,password=password,port=port,timeout=10)
stdin,stdout,stderr = ssh.exec_command("ifconfig")
data = stdout.read().decode('utf8')
error = stderr.read().decode('utf8')
if data:
    print('[%s:OUT]:\n%s' % (host,data))
 
if error:
    print('[%s:ERROR]:\n%s' % (host,error))
 
ssh.close()

