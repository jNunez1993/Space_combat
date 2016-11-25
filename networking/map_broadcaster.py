import json

class MapBroadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.broadcast()


	def broadcast(self):
		while True:
			for thread in self.playerThreads:
				if thread.didPlayerMove():
					mapData = self.gameMap.serialize()
					msg = "map data"
					blob = {
						"msg" : msg,
						"map" : mapData
					}
					socket = thread.getSocket()
					socket.sendall(json.dumps(blob))
