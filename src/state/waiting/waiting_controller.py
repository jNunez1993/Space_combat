from waiting_view import WaitingView 
from state import PlayState 

class WaitingController:
	def __init__(self,stateMachine,client):
		self.client = client
		self.stateMachine = stateMachine
		self.view = WaitingView()

	def update(self):
		self.view.render()
		if self.client.arePlayersConnected():
			print "All players are connected"
			self.stateMachine.push(PlayState(self.stateMachine,self.client))


