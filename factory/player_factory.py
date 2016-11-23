from .factory import Factory
from model import Player
from model import Location
import player_config

class PlayerFactory(Factory):
	def __init__(self):
		pass

	@staticmethod
	def construct():
		playerConfigs = player_config.PLAYERS
		players = []
		for pc in playerConfigs:
			id_ = pc["id"]
			x = pc["location"]["x"]
			y = pc["location"]["y"]
			location = Location(x,y)
			direction = pc["direction"]
			hp = pc["hp"]
			player = Player(id_,location,direction,hp)
			players.append(player)
		return players
		
