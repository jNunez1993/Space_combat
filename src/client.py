import socket
import json

class Client:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server_address = ('localhost',10000)
		self.socket.connect(server_address)
		data = self.socket.recv(1024)
		data = json.loads(data)
		print data
