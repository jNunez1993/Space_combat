import pygame

class EndView:
	def __init__(self):
		self.status = None
		self.window = pygame.display.get_surface()
		self.font = pygame.font.Font(None, 36)
		self.RED = (255,0,0)
		self.rendered = False

	def render(self):
		if self.status != None:
			msg = self.getStatusString()
			self.window.fill((0,0,0))
			text = self.font.render(msg,1,self.RED)
			self.window.blit(text,(640/2-54,480/2-54))
			pygame.display.flip()
			self.rendered = True



	def getStatus(self):
		return self.status

	def setStatus(self,status):
		self.status = status

	def getStatusString(self):
		status = self.getStatus()
		if status == 1:
			return "You win"
		else:
			return "You lose"

	def isRendered(self):
		return self.rendered

