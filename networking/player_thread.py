from threading import Thread

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
	def run(self):
		pass
		#while True:
			#print "Listening for client_id : " + str(self.player.getId())