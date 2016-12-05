import pygame
import time
from threading import Thread

class KeyEvent:
	def __init__(self):
		self.lastPress = 0
		self.didMove = True
		self.spacebarActivated = True

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

			if self.spacebarActivated and keyPressed[pygame.K_SPACE]:
				keys+="x"
				Thread(target=self.spacebarWait).start()

			if self.didMove:
				self.lastPress = currPress
				self.didMove = False
				return keys

			if keys == "x":
				self.lastPress = currPress
				return keys


		return None

	def spacebarWait(self):
		self.spacebarActivated = False
		time.sleep(.15)
		self.spacebarActivated = True

