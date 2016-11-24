from play_view import PlayView
from utility import KeyEvent

class PlayController:
	def __init__(self,stateMachine,client):
		self.stateMachine = stateMachine
		self.client = client 
		self.view = PlayView()
		keyEvent = KeyEvent()
		


	def update(self):
		self.view.render()
