from .location import Location
from .direction import Direction
from interface import Serializable

class Projectile(Serializable):

	def __init__(self,id_,location,direction):
		self.location = location
		self.direction = direction
		self.id = id_
		self.speed = 5

	def getLocation(self):
		return self.location
		
	def setLocation(self,x,y, location = None):
		if location:
			self.location = location
		else:
			self.location.setLocation(x,y)

	def updateLocation(self):
		displacementValues = self.direction.getDisplacement()
		x = displacementValues[0]
		y = displacementValues[1]
		self.location.displace(x*self.speed,y*self.speed)

	def getDirection(self):
		return self.direction

	def serialize(self):
		serialized = {
			"id" : self.id,
			"location" : {
				"x" : self.getLocation().getX(),
				"y" : self.getLocation().getY()
			},
			"direction" : self.getDirection().getDirectionString()
		}
		return serialized
		