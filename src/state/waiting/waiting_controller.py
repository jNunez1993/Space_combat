from waiting_view import WaitingView

class WaitingController:
	def __init__(self,stateMachine):
		self.stateMachine = stateMachine
		self.view = WaitingView()

	def update(self):
		self.view.render()
