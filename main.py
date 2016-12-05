from factory import PlayerFactory
from factory import MapFactory
from networking import PlayerThread
from server import Server

#Testing stuff for now
#Still have not created the server instance
players = PlayerFactory.construct()

# for player in players:
# 	p = PlayerThread(player)
# 	p.start()


# gameMap = MapFactory.construct()
# gameMap.updatePlayers(players)

# print gameMap.getPlayers()

while True:
	server = Server()
	server.start()


