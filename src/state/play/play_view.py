import pygame
from map_view import MapView

class PlayView:
	def __init__(self):
		self.window = pygame.display.get_surface()
		self.mapView = MapView(self.window)
		

	def render(self):
		self.window.fill((0,0,0))
		self.mapView.render()
		pygame.display.flip()


	def setMap(self,gameMap):
		self.mapView.setMap(gameMap)
		
