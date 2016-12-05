from home_view import HomeView
from utility import Button
from state import WaitingState 
import pygame
import sys

class HomeController:

	def __init__(self,stateMachine):
		self.stateMachine = stateMachine
		self.view = HomeView()
		self.buttons = []
		self.initializePlayButton()
		self.initializeQuitButton()

	def update(self):
		self.handleInput()
		self.view.render()

	def handleInput(self):
		mouse_pressed = pygame.mouse.get_pressed()
		if mouse_pressed[0]:
			x,y = pygame.mouse.get_pos()
			for btn in self.buttons:
				if btn.collidepoint(x,y):
					btn.onClick()


	def initializePlayButton(self):
		playBtn = Button(200,100,250,100)
		playBtn.onClick = self.toWaitingState
		self.buttons.append(playBtn)
		self.view.setPlayBtn(playBtn)

	def initializeQuitButton(self):
		quitBtn = Button(200,200,250,100)
		quitBtn.onClick = self.quitGame
		self.buttons.append(quitBtn)
		self.view.setQuitBtn(quitBtn)


	def toWaitingState(self):
		self.stateMachine.push(WaitingState(self.stateMachine))

	def quitGame(self):
		sys.exit(0)