import socket
import json
import config
from threading import Thread
import time

class Client:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.listenerThread = Thread(target=self.listen)
		self.workerThread = Thread(target=self.process)
		self.queue = []
		self.mapReady = False
		self.mapData = None
		self.keypressACK = True
		self.keyPressLock = False
		self.sendLock = False
		self.gameOver = False
		self.won = 0

	def connect(self):
		try:
			self.socket.connect(config.serverAddress)
		except:
			print "Could not establish connection to the server"


	def arePlayersConnected(self):
		data = self.socket.recv(1024)
		data = json.loads(data)
		if data["msg"] == "All players have connected":
			return True
		return False

	def start(self):
		self.listenerThread.start()
		self.workerThread.start()

	def listen(self):
		while True:
			data = self.socket.recv(1024)
			data = json.loads(data)
			self.queue.append(data)

	def process(self):
		while True:
			if len(self.queue) > 0:
				data = self.queue.pop(0)
				if data["msg"] == "map data":
					self.mapReady = True
					self.mapData = data["map"]
					while self.sendLock:
						continue
					self.sendLock = True
					self.socket.sendall(json.dumps({"msg" : "mapACK"}))
					time.sleep(.008)
					self.sendLock = False
				elif data["msg"] == "kpACK":
					while self.keyPressLock:
						continue
					self.keyPressLock = True
					self.keypressACK = True
					self.keyPressLock = False

				elif data["msg"] == "game over":
					self.gameOver = True
					if data["won"] == 1:
						self.won = 1




	def sendKeyPressed(self,key):
		print "Sending key " + str(key)
		if self.keypressACK and self.keyPressLock == False:
			self.keyPressLock = True
			data = {"keyPressed" : key , "msg" : "key pressed"}
			while self.sendLock:
						continue
			self.sendLock = True
			self.socket.sendall(json.dumps(data))
			time.sleep(.008)
			self.sendLock = False
			self.keypressACK = False
			self.keyPressLock = False

	def isMapDataReady(self):
		return self.mapReady 

	def getMapData(self):
		self.mapReady = False
		return self.mapData

	def isGameOver(self):
		return (self.gameOver,self.won)








	
		



