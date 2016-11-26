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
		self.projectiles = []
		self.projectilesReady = False

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
						if "x" in keysPressed:
							projectile = self.player.attack()
							self.projectiles.append(projectile)
							self.projectilesReady = True
							keysPressed = keysPressed.replace("x","")
							print "Projectile appended"
						print "keysPressed: " + str(keysPressed)
						keysPressed = keysPressed[0:2] #error handling. Possible for user to spam 3 keys at same time
						if keysPressed == "":
							msg = {"msg" : "kpACK"}
							while self.sendLock:
								continue
							self.sendLock = True
							self.socket.sendall(json.dumps(msg))
							time.sleep(.008)
							self.sendLock = False
						else:
							direction = locationMapper.toLongDirection(keysPressed)
							displacement = locationMapper.displacementFromDirection(direction)
							self.player.move(displacement[0],displacement[1])
							self.player.setDirection(direction)
							msg = {"msg" : "kpACK"}
							while self.sendLock:
								continue
							self.sendLock = True
							self.socket.sendall(json.dumps(msg))
							time.sleep(.008)
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

	def getProjectiles(self):
		if self.projectilesReady:
			toRet = self.projectiles
			self.projectiles = []
			self.projectilesReady = False
			return toRet
		return []

