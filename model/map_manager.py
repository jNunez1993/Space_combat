from threading import Thread
import time

class MapManager:
	def __init__(self,gameMap):
		self.gameMap = gameMap

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


	def executeProjectile(self,projectile):
		while not self.gameMap.outOfBounds(projectile.getLocation().getX(),projectile.getLocation().getY()):
			projectile.updateLocation()
			time.sleep(.1)