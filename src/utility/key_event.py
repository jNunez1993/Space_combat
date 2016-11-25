import pygame
import time

class KeyEvent:
	def __init__(self):
		self.lastPress = 0
		self.didMove = True

	def getKeyPressed(self):
		currPress = time.time()
		keyPressed = pygame.key.get_pressed()
		keys = ""
		if currPress-self.lastPress > 0.05:
			if keyPressed[pygame.K_s]:
				self.didMove = True
				keys+="s"
			if keyPressed[pygame.K_d]:
				self.didMove = True
				keys+="d"

			if keyPressed[pygame.K_w]:
				self.didMove = True 
				keys+="w"

			if keyPressed[pygame.K_a]:
				self.didMove = True
				keys+="a"

			if self.didMove:
				self.lastPress = currPress
				self.didMove = False
				return keys


		return None

