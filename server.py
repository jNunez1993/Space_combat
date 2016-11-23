import json
import socket
import config
from networking import PlayerThread

class Server:
	def __init__(self):
		self.MAX_CONNECTIONS = 2
		self.playerSockets = []
		self.playerThreads = []

	def start(self):
		self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.serverSocket.bind(config.server_address)
		self.serverSocket.listen(config.MAX_CONNECTIONS)
		self.waitForPlayers() 
	
	def waitForPlayers(self):
		while True:
			playerSocket,client_addr = self.serverSocket.accept()
			self.playerSockets.append(playerSocket)
			print "Player connected from " + str(client_addr)
			if len(self.playerSockets) == 2:
				break
		
		#self.allPlayersConnected()

	def allPlayersConnected(self):
		for player in self.playerSockets:
			msg = {"msg" : "All players have connected"}
			player.sendall(json.dumps(msg))



