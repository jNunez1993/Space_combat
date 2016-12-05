

class Location:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def getLocation(self):
		return self

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setLocation(self,x,y):
		self.x = x
		self.y = y

	def displace(self,x,y):
		self.x += x
		self.y += y

	
		