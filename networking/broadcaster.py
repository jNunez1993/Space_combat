import json
import time
from model import MapManager

class Broadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.mapManager = MapManager(self.gameMap)
		self.mapManager.startCollisionHandling()
		self.broadcast()


	def broadcast(self):
		done = False
		while not done:
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

				dead = thread.isPlayerDead()
				if dead:
					self.loserId = thread.getId()
					done = True
					break

		self.broadcastGameOver()



	def broadcastGameOver(self):
		for thread in self.playerThreads:
			thread.stop()

		for thread in self.playerThreads:
			socket = thread.getSocket()
			msg = None
			if self.loserId != thread.getId():
				msg = {
					"msg": "game over",
					"won": 1
				}
			else:
				msg = {
				"msg": "game over",
				"won": 0
				}
			socket.sendall(json.dumps(msg))

		for thread in self.playerThreads:
			socket = thread.getSocket()
			socket.close()










