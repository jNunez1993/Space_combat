from interface import Serializable

class Map(Serializable):

	def __init__(self):
		self.projectiles = []
		self.xBound = 640
		self.yBound = 480

	def updatePlayer(self,id_,player):
		self.players[id_] = player

	def updatePlayers(self,players):
		self.players = players

	def updateProjectiles(self,projectiles):
		self.projectiles = projectiles

	def getPlayers(self):
		return self.players

	def addProjectile(self,projectile):
		self.projectiles.append(projectile)

	def getProjectiles(self):
		return self.projectiles

	def setProjectiles(self,projectiles):
		self.projectiles = projectiles

	def outOfBounds(self,x,y):
		if (x<0 or x>self.xBound) or (y<0 or y>self.yBound):
			return True
		return False

	def serialize(self):
		serialized = {}
		players = [player.serialize() for player in self.players]
		projectiles = [projectile.serialize() for projectile in self.projectiles]
		serialized["players"] = players
		serialized["projectiles"] = projectiles
		return serialized





