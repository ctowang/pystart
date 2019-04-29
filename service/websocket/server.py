from bottle import request, Bottle, abort
from geventwebsocket import WebSocketError
from gevent.pywsgi import WSGIServer
from flask import request
from geventwebsocket.handler import WebSocketHandler
from bottle import get, post, request
app = Bottle()
users = {}
@app.get('/')
def handle_websocket(token,senduser):
	wsock = request.environ.get('wsgi.websocket')
	users[token] = wsock
	if not wsock:
		abort(400, 'Expected WebSocket request.')
		while True:
			try:
				message = wsock.receive()
			except WebSocketError:
				break
				if message:
					try:
						users[senduser].send(message)
					except WebSocketError:
						print (u'kill')
server = WSGIServer(("192.168.213.30", 28033), app,handler_class=WebSocketHandler)						
server.serve_forever()

