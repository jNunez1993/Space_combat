

class Direction:
	def __init__(self,direction):
		self.directions = {}
		self.directions["north"] = (0,-1)
		self.directions["south"] = (0,1)
		self.directions["east"] = (1,0)
		self.directions["west"] = (-1,0)
		self.currentDirection = direction

	def setDirection(self,direction):
		self.currentDirection = direction


	def getDirectionString(self):
		return self.currentDirection

	def getDisplacement(self):
		return self.directions[self.currentDirection]


