

class MapBroadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.broadcast()


	def broadcast(self):
		while True:
			for thread in self.playerThreads:
				if thread.didPlayerMove():
					print self.gameMap.serialize()
