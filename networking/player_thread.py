import json
from utilities import LocationMapper as locationMapper
import time
from threading import Thread

#Responsible for receiving player information and updating its player
class PlayerThread:
	def __init__(self,socket,player):
		self.socket = socket
		self.player = player
		self.mapACK = True
		self.queue = []
		self.listenerThread = Thread(target=self.listen)
		self.workerThread = Thread(target=self.process)

		self.sendLock = False

	def start(self):
		self.listenerThread.start()
		self.workerThread.start()


	def getPlayer(self):
		return self.player

	def getSocket(self):
		return self.socket

	#overridden method
	#will listen for key pressed and update the player as needed
	#Would be good if it can inform the map broadcaster that a change has occured
	def listen(self):
		while True:
			data = self.socket.recv(1024)
			data = json.loads(data)
			self.queue.append(data)


	def process(self):
		while True:
			if len(self.queue) > 0:
				data = self.queue.pop(0)
				if data["msg"] == "key pressed":
						keysPressed = data["keyPressed"]
						direction = locationMapper.toLongDirection(keysPressed)
						displacement = locationMapper.displacementFromDirection(direction)
						self.player.move(displacement[0],displacement[1])
						self.player.setDirection(direction)
						msg = {"msg" : "kpACK"}
						while self.sendLock:
							continue
						self.sendLock = True
						self.socket.sendall(json.dumps(msg))
						time.sleep(.005)
						self.sendLock = False


				elif data["msg"] == "mapACK":
					self.mapACK = True


	def getSendLock(self):
		return self.sendLock

	def setSendLock(self,val):
		self.sendLock = val


	def didReceiveMapACK(self):
		if self.mapACK:
			self.mapACK = False
			return True
		return False

