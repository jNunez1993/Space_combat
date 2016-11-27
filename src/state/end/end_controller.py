from end_view import EndView 
import time

class EndController:
	def __init__(self,stateMachine,status):
		self.stateMachine = stateMachine 
		self.status = status
		self.endView = EndView()
		self.endView.setStatus(status)


	def update(self):
		self.endView.render()
		if self.endView.isRendered():
			time.sleep(3)
			while self.stateMachine.size() != 0:
				self.stateMachine.pop()


