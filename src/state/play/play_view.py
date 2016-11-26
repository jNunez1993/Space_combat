import pygame
from life_view import LifeView
from map_view import MapView

class PlayView:
	def __init__(self):
		self.window = pygame.display.get_surface()
		self.mapView = MapView(self.window)
		self.lifeView = LifeView(self.window)
		

	def render(self):
		self.window.fill((0,0,0))
		self.mapView.render()
		self.lifeView.render()
		pygame.display.flip()


	def setMap(self,gameMap):
		self.mapView.setMap(gameMap)
		self.lifeView.setPlayers(gameMap["players"])

		
