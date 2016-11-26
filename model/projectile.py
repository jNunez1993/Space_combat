from .location import Location
from .direction import Direction
from interface import Serializable
from utilities import LocationMapper as locationMapper

class Projectile(Serializable):

	def __init__(self,id_,location,direction):
		self.location = location
		self.direction = direction
		self.id = id_
		self.speed = 8
		self.hasCollided = False

	def getId(self):
		return self.id

	def getLocation(self):
		return self.location
		
	def setLocation(self,x,y, location = None):
		if location:
			self.location = location
		else:
			self.location.setLocation(x,y)

	def updateLocation(self):
		displacementValues = locationMapper.displacementFromDirection(self.direction.getDirectionString())
		x = displacementValues[0]
		y = displacementValues[1]
		self.location.displace(x*self.speed,y*self.speed)

	def getDirection(self):
		return self.direction

	def getCollided(self):
		return self.hasCollided 

	def setCollided(self,val):
		self.hasCollided = True

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
		