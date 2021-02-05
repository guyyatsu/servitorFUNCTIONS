import socket
import threading


host = #To be populated by the user
port = #Be sure to alter the corresponding variables in chat.client.py



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

nicknames = []


def broadcast(message):
	for client in clients:
		client.send(message)


def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast('{} left!'.format(nickname).encode('ascii'))
			nicknames.remove(nickname)
			break


def recieve():
	while True:
		client, address = server.accept()
		print("Connected to {}".format(str(address)))
		
		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)
		
		print("User: {}".format(nickname))
		broadcast("{} has joined the chat.".format(nickname).encode('ascii'))
		client.send('Connected to GUYYATSU.me: '.encode('ascii'))
		
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

recieve()
