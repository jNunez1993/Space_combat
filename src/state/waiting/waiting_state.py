from state import State
from waiting_controller import WaitingController
from networking import Client

class WaitingState(State):
	def __init__(self,stateMachine):
		client = Client()
		client.connect()
		self.controller = WaitingController(stateMachine,client)


	def update(self):
		self.controller.update()

