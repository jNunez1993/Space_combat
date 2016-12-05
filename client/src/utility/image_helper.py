

class ImageHelper:

	#returns path of ship
	@staticmethod
	def getShip(id_,direction):
		return "../img/ship" + str(id_) + "_" + str(direction) + ".png"

