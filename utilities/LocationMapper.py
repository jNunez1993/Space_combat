
directionMapping = {
	"w" : "north",
	"a" : "west",
	"s" : "south",
	"d" : "east",
	"wd" : "northeast",
	"dw" : "northeast",
	"wa" : "northwest",
	"aw" : "northwest",
	"sd" : "southeast",
	"ds" : "southeast",
	"sa" : "southwest",
	"as" : "southwest"
}

directions = {}
directions["north"] = (0,-1)
directions["south"] = (0,1)
directions["east"] = (1,0)
directions["west"] = (-1,0)
directions["northeast"] = (1,-1)
directions["northwest"] = (-1,-1)
directions["southeast"] = (1,1)
directions["southwest"] = (-1,1)


def toLongDirection(keys):
	if keys in directionMapping:
		return directionMapping[keys]
	return "north"

def displacementFromDirection(direction):
	return directions[direction]
