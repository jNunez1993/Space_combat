import pygame

class PlayView:
	def __init__(self):
		self.window = pygame.display.get_surface()
		self.starship = pygame.image.load("../img/ship1_north.png")
		

	def render(self):
		self.window.fill((0,0,0))
		self.window.blit(self.starship, self.starship.get_rect())
		pygame.display.flip()
		
