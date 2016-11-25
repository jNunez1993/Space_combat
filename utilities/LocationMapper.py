


def directionToDisplacement(direction):
	displacement = {}
	if direction == "w" or direction=="North":
		displacement["x"] = 0
		displacement["y"] = -1

	elif direction == "a" or direction=="West":
		displacement["x"] = -1
		displacement["y"] = 0

	elif direction == "s" or direction=="South":
		displacement["x"] = 0
		displacement["y"] = 1

	elif direction == "d" or direction=="East":
		displacement["x"] = 1
		displacement["y"] = 0

	return displacement

