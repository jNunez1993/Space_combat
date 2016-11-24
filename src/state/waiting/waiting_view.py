import pygame

class WaitingView:
	def __init__(self):
		self.window = pygame.display.get_surface()
		self.font = pygame.font.Font(None, 36)
		self.WHITE = (255,255,255)




	def render(self):
		self.window.fill((0,0,0))
		text = self.font.render("Waiting for players to connect",1,self.WHITE)
		self.window.blit(text,(140,210))
		pygame.display.flip()