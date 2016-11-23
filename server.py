import json
import socket
import config
from networking import PlayerThread
from networking import MapBroadcaster
from factory import PlayerFactory
from factory import MapFactory

class Server:
	def __init__(self):
		self.playerSockets = []
		self.playerThreads = []
		self.mapBroadcaster = None

	def start(self):
		self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.serverSocket.bind(config.server_address)
		self.serverSocket.listen(config.MAX_CONNECTIONS)
		self.waitForPlayers() 
	
	def waitForPlayers(self):
		print "Waiting for players..."
		while True:
			playerSocket,client_addr = self.serverSocket.accept()
			self.playerSockets.append(playerSocket)
			print "Player connected from " + str(client_addr)
			if len(self.playerSockets) == 2:
				break
		print "All players have connected"
		self.initializeGame()

	def initializeGame(self):
		players = PlayerFactory.construct()
		gameMap = MapFactory.construct()
		gameMap.updatePlayers(players)

		for i,player in enumerate(players):
			pthread = PlayerThread(self.playerSockets[i],player)
			self.playerThreads.append(pthread)

		self.allPlayersConnected()

		for thread in self.playerThreads:
			thread.start()
		self.mapBroadcaster = MapBroadcaster(gameMap,self.playerThreads)

	def allPlayersConnected(self):
		for player in self.playerSockets:
			msg = {"msg" : "All players have connected"}
			player.sendall(json.dumps(msg))



