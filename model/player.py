from .projectile import Projectile
from .direction import Direction
from .location import Location
from interface import Serializable


class Player(Serializable):
	def __init__(self,id_,location = None,direction = None,hp = None):
		self.id = id_
		if location:
			self.location = location
		else:
			self.location = Location(0,0)

		if direction:
			self.direction = Direction(direction)
		else:
			self.direction = Direction("East")

		if hp:
			self.hp = hp
		else:
			self.hp = 100

	def getId(self):
		return self.id

	def attack(self):
		projectile = Projectile(self.id,Location(self.getLocation().getX(),self.getLocation().getY()),Direction(self.direction.getDirectionString()))
		return projectile

	def move(self,x,y):
		self.location.displace(x*3,y*3)

	def getLocation(self):
		return self.location

	def getDirection(self):
		return self.direction

	def setDirection(self,direction):
		self.direction.setDirection(direction)

	def getHp(self):
		return self.hp

	def setHp(self,hp):
		self.hp = hp

	def serialize(self):
		serialized = {
			"id" : self.id,
			"location" : {
				"x" : self.getLocation().getX(),
				"y" : self.getLocation().getY()
			},
			"direction" : self.getDirection().getDirectionString(),
			"hp" : self.getHp()
		}
		return serialized
	
