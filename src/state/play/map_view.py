from utility import ImageHelper
import pygame


class MapView:
	def __init__(self, window = None):
		if window == None:
			self.window = pygame.display.get_surface()
		else:
			self.window = window

		self.gameMap = None
		self.players = []
		self.projectiles = []



	def render(self):
		img = None
		for player in self.players:
			img = self.getPlayerRepresentation(player)
			x = player["location"]["x"]
			y = player["location"]["y"]

			#eventually need x,y to be bounds in a rectangle
			self.window.blit(img,(x,y))

		for projectile in self.projectiles:
			x = projectile["location"]["x"]
			y = projectile["location"]["y"]
			dis = self.bulletDisplacement(projectile["direction"],img.get_rect())

			if projectile["id"] == 1:
				pygame.draw.circle(self.window,(255,0,0),(x+dis[0],y+dis[1]),3)
			if projectile["id"] == 2:
				pygame.draw.circle(self.window,(0,255,0),(x+dis[0],y+dis[1]),3)

		pygame.display.flip()



	def getPlayerRepresentation(self,player):
		direction = player['direction']
		playerId = player['id']
		imgstr = ImageHelper.getShip(playerId,direction)
		return pygame.image.load(imgstr)



	def getMap(self):
		return self.gameMap

	def setMap(self,gameMap):
		self.gameMap = gameMap
		self.players = self.gameMap['players']
		self.projectiles = self.gameMap['projectiles']


	def bulletDisplacement(self, direction,rect):
		width = rect.width
		height = rect.height
		disX = 0
		disY = 0
		if direction == "north":
			disX = width/2
		elif direction == "east":
			disX = width
			disY = height/2
		elif direction == "south":
			disX = width/2
			disY = height
		elif direction == "west":
			disY = height/2
		elif direction == "northeast":
			disX = width
		elif direction == "northwest":
			pass
		elif direction == "southeast":
			disX = width
			disY = height
		elif direction == "southwest":
			disY = height

		return (disX,disY)




