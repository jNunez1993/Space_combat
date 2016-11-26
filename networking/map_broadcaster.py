import json
import time
from model import MapManager

class MapBroadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.mapManager = MapManager(self.gameMap)
		self.mapManager.startCollisionHandling()
		self.broadcast()


	def broadcast(self):
		while True:
			for thread in self.playerThreads:
				while not thread.didReceiveMapACK():
						continue
				
				projectiles = thread.getProjectiles()
				self.mapManager.handleProjectiles(projectiles)

				mapData = self.gameMap.serialize()
				msg = "map data"
				blob = {
					"msg" : msg,
					"map" : mapData
				}
				socket = thread.getSocket()
				while thread.getSendLock():
					continue
				thread.setSendLock(True)
				socket.sendall(json.dumps(blob))
				time.sleep(.008)
				thread.setSendLock(False)


