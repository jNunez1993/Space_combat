from threading import Thread
import json

#Responsible for receiving player information and updating its player
#All of these players will be fed to the map object
#which is something that will
class PlayerThread(Thread):
	def __init__(self,socket,player):
		Thread.__init__(self)
		self.socket = socket
		self.player = player

	def getPlayer(self):
		return self.player

	#overridden method
	#will listen for key pressed and update the player as needed
	#Would be good if it can inform the map broadcaster that a change has occured
	def run(self):
		print "Checking for key pressed"
		while True:
			print "waiting for key"
			data = self.socket.recv(1024)
			data = json.loads(data)
			keyPressed = data["keyPressed"]
			print "key received:" + str(keyPressed)
			msg = {"msg" : "kpACK"}
			self.socket.sendall(json.dumps(msg))
