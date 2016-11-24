from state import State
from waiting_controller import WaitingController

class WaitingState(State):
	def __init__(self,stateMachine):
		self.controller = WaitingController(stateMachine)


	def update(self):
		self.controller.update()

