from play_view import PlayView
from utility import KeyEvent
from state import EndState 

class PlayController:
	def __init__(self,stateMachine,client):
		self.stateMachine = stateMachine
		self.client = client 
		self.view = PlayView()
		self.keyEvent = KeyEvent()
		client.start()


	def update(self):
		key = self.keyEvent.getKeyPressed()
		if key != None:
			self.client.sendKeyPressed(key)
		if self.client.isMapDataReady():
			self.view.setMap(self.client.getMapData())
		tup = self.client.isGameOver()
		gameOver = tup[0]
		if gameOver:
			wonStatus = tup[1]
			self.stateMachine.push(EndState(self.stateMachine,wonStatus))

		self.view.render()
