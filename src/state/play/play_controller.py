from play_view import PlayView
from utility import KeyEvent

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
		self.view.render()
