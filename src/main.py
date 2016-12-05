import pygame
from state import StateMachine
from state import HomeState

def init():
	pygame.init()
	pygame.font.init()
	clock = pygame.time.Clock()
	clock.tick(30)
	pygame.display.set_mode((640, 480))

def main():
	init()
	stateMachine = StateMachine()
	stateMachine.push(HomeState(stateMachine))
	
	while True:
		if stateMachine.size() > 0:
			currentState = stateMachine.peek()
			currentState.update()
		else:
			stateMachine.push(HomeState(stateMachine))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


if __name__ == "__main__":
	main()
