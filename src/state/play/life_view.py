import pygame

class LifeView:
	def __init__(self,window = None):
		if window == None:
			self.window = pygame.display.get_surface()
		else:
			self.window = window
		self.players = []
		p1lifebarPos = (20,50)
		p2lifebarPos = (500,50)
		self.lifebarPositions = {}
		self.lifebarPositions[1] = p1lifebarPos
		self.lifebarPositions[2] = p2lifebarPos
		self.lifebarHeight = 20

	def render(self):
		for player in self.players:
			lifebarPos = self.lifebarPositions[int(player["id"])]
			hp = player["hp"]
			lifeLeftRect = pygame.Rect(lifebarPos,(hp,self.lifebarHeight))
			if hp != 100:
				emptyLife = pygame.Rect((lifebarPos[0]+hp,lifebarPos[1]),(100-hp,self.lifebarHeight))
				pygame.draw.rect(self.window,(255,0,0),emptyLife)
			pygame.draw.rect(self.window,(0,255,0),lifeLeftRect)

	def setPlayers(self, players):
		self.players = players



				



