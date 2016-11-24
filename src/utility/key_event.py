import pygame

class KeyEvent:
	def __init__(self):
		pass

	def getKeyPressed(self):
		keyPressed = pygame.key.get_pressed()
		if keyPressed[pygame.K_w]:
			return "w"
		if keyPressed[pygame.K_a]:
			return "a"
		if keyPressed[pygame.K_s]:
			return "s"
		if keyPressed[pygame.K_d]:
			return "d"

