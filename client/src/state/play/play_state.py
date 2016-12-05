from state import State 
from play_controller import PlayController


class PlayState(State):
	def __init__(self,stateMachine,client):
		self.controller = PlayController(stateMachine,client)

	def update(self):
		self.controller.update()