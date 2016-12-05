from server import Server


def main():
	while True:
		server = Server()
		server.start()

if __name__ == "__main__":
	main()
