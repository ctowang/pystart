from websocket import create_connection
ws_server = "ws://192.168.213.30:28012/websocket"
ws = create_connection(ws_server)
ws.send("?userCode=124321&relationId=32011112029");
while True: 
    print(ws.recv())
