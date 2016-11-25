from threading import Thread
import json
from utilities import LocationMapper as locationMapper

#Responsible for receiving player information and updating its player
class PlayerThread(Thread):
	def __init__(self,socket,player):
		Thread.__init__(self)
		self.socket = socket
		self.player = player
		self.didMove = False

	def getPlayer(self):
		return self.player

	def getSocket(self):
		return self.socket

	#overridden method
	#will listen for key pressed and update the player as needed
	#Would be good if it can inform the map broadcaster that a change has occured
	def run(self):
		print "Checking for key pressed"
		while True:
			data = self.socket.recv(1024)
			data = json.loads(data)
			keysPressed = data["keyPressed"]
			direction = locationMapper.toLongDirection(keysPressed)
			displacement = locationMapper.displacementFromDirection(direction)
			self.player.move(displacement[0],displacement[1])
			self.player.setDirection(direction)
			msg = {"msg" : "kpACK"}
			self.socket.sendall(json.dumps(msg))
			self.didMove = True

	def didPlayerMove(self):
		if self.didMove:
			self.didMove = False
			return True
