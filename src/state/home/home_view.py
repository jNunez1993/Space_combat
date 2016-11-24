import pygame
from utility import Button

class HomeView:
	def __init__(self):
		self.window = pygame.display.get_surface()
		self.playBtn = None
		self.quitBtn = None
		self.playBtnImg = pygame.image.load("../img/button-start-game.png")
		self.quitBtnImg = pygame.image.load("../img/button-quit-game.png")

	def render(self):
		self.window.fill((0,0,0))
		self.window.blit(self.playBtnImg,self.playBtn)
		self.window.blit(self.quitBtnImg,self.quitBtn)
		pygame.display.flip()

	def setPlayBtn(self,btn):
		self.playBtn = btn
		self.transformPlayImg()

	def setQuitBtn(self,btn):
		self.quitBtn = btn
		self.transformQuitImg()

	def transformPlayImg(self):
		self.playBtnImg = pygame.transform.scale(self.playBtnImg,(self.playBtn.width,self.playBtn.height))

	def transformQuitImg(self):
		self.quitBtnImg = pygame.transform.scale(self.quitBtnImg,(self.quitBtn.width,self.quitBtn.height))

		