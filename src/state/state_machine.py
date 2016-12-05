
class StateMachine:

	def __init__(self):
		self.states = []

	def push(self,state):
		self.states.append(state)

	def pop(self):
		return self.states.pop()

	def peek(self):
		return self.states[-1]

	def size(self):
		return len(self.states)
	