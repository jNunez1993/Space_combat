from rectangle import Rectangle

class Button(Rectangle):
	def __init__(self,left, top, width, height):
		Rectangle.__init__(self,left,top,width,height)