from threading import Thread
from collision_manager import CollisionManager
import time

class MapManager:
	def __init__(self,gameMap):
		self.gameMap = gameMap
		self.collisionManager = CollisionManager()
		self.collisionManager.setPlayers(self.gameMap.getPlayers())
		self.collisionManager.setProjectiles(self.gameMap.getProjectiles())

	def handleProjectiles(self,projectiles):
		for projectile in projectiles:
			print "inside projectiles"
			Thread(target=self.executeProjectile,args=[projectile]).start()
			self.gameMap.addProjectile(projectile)


		projectiles = self.gameMap.getProjectiles()
		toKeep = []

		for projectile in projectiles:
			x = projectile.getLocation().getX()
			y = projectile.getLocation().getY()
			if not self.gameMap.outOfBounds(x,y):
				toKeep.append(projectile)

		self.gameMap.setProjectiles(toKeep)
		self.collisionManager.setProjectiles(toKeep)

	def startCollisionHandling(self):
		Thread(target=self.collisionManager.run).start()


	def executeProjectile(self,projectile):
		while not self.gameMap.outOfBounds(projectile.getLocation().getX(),projectile.getLocation().getY()):
			projectile.updateLocation()
			time.sleep(.1)