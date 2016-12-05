from end_controller import EndController 


class EndState:
	def __init__(self,stateMachine,status):
		self.stateMachine = stateMachine 
		self.status = status
		self.controller = EndController(stateMachine,status)

	def update(self):
		self.controller.update()

