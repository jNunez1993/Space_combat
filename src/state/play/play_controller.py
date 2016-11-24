from play_view import PlayView


class PlayController:
	def __init__(self,stateMachine,client):
		self.stateMachine = stateMachine
		self.client = client 
		self.view = PlayView()

	def update(self):
		self.view.render()
