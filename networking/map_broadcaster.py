

class MapBroadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.broadcast()


	def broadcast(self):
		pass
		# while True:
		# 	for thread in self.playerThreads:
		# 		print "Sending map information to player: " + str(thread.getPlayer().getId())
