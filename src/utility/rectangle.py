import pygame
from interface import Drawable

class Rectangle(pygame.Rect, Drawable):
	def __init__(self,left, top, width, height):
		self.color = (0,0,0)
		pygame.Rect.__init__(self, left, top, width, height)

	def draw(self, window = None):
		if window == None:
			window = pygame.display.get_surface()
		pygame.draw.rect(window, self.getColor(), self)

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def onClick(self):
		pass