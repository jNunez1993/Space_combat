from factory import Factory
from model import Map

class MapFactory(Factory):

	@staticmethod
	def construct():
		return Map()



