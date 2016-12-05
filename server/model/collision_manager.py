

class CollisionManager:
	def __init__(self):
		self.players = []
		self.projectiles = []
		self.playerSize = 45
		self.projectileRadius = 3

	def run(self):
		while True:
			for player in self.players:
				playerId = player.getId()
				for projectile in self.projectiles:
					if projectile.getId() != playerId:
						if not projectile.getCollided() and self.hasCollided(projectile,player):
							projectile.setCollided(True)
							hp = player.getHp()
							player.setHp(hp-10)




	def setPlayers(self,players):
		self.players = players 

	def setProjectiles(self,projectiles):
		self.projectiles = projectiles


	def hasCollided(self,projectile,player):
		projX = projectile.getLocation().getX()
		projY = projectile.getLocation().getY()

		projXspan = (projX-self.projectileRadius,projX+self.projectileRadius)
		projYspan = (projY-self.projectileRadius,projY+self.projectileRadius)

		pX = player.getLocation().getX()
		pY = player.getLocation().getY()

		pXspan = (pX-self.playerSize/2,pX+self.playerSize/2)
		pYspan = (pY-self.playerSize/2,pY+self.playerSize/2)

		if (projXspan[0] > pXspan[0] and projXspan[0] > pXspan[1]) or (projYspan[0] > pYspan[0] and projYspan[0] > pYspan[1]):
			return False

		if (projXspan[0] < pXspan[0] and projXspan[1] < pXspan[0]) or (projYspan[0] < pYspan[0] and projYspan[1] < pYspan[0]):
			return False

		return True







