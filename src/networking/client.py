import socket
import json
import config

class Client:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def connect(self):
		try:
			self.socket.connect(config.serverAddress)
		except:
			print "Could not establish connection to the server"


	def arePlayersConnected(self):
		data = self.socket.recv(1024)
		data = json.loads(data)
		if data["msg"] == "All players have connected":
			return True
		return False

	
		



