import json
import time

class MapBroadcaster:
	def __init__(self,gameMap, playerThreads):
		self.gameMap = gameMap
		self.playerThreads = playerThreads
		self.broadcast()


	def broadcast(self):
		while True:
			for thread in self.playerThreads:
				while not thread.didReceiveMapACK():
						continue
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
				time.sleep(.005)
				thread.setSendLock(False)

