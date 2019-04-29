import subprocess
from websocket import create_connection
ws_server = "ws://172.18.30.19:1010/websocket/" 
ws = create_connection(ws_server) 
command='sshpass -p 123456 ssh 192.168.20.200 -p 32776 -o StrictHostKeychecking=no "tail -f /root/tomcat-8.0/logs/catalina.out"' 
popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True) 

while True: 
    line=popen.stdout.readline().strip() 
    ws.send(line)
