from state import State
from home_controller import HomeController

class HomeState(State):

	def __init__(self,stateMachine):
		self.controller = HomeController(stateMachine)
		

	def update(self):
		self.controller.update()