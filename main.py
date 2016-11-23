from factory import PlayerFactory
from networking import PlayerThread

#Testing stuff for now
#Still have not created the server instance
players = PlayerFactory.construct()

for player in players:
	p = PlayerThread(player)
	p.start()


