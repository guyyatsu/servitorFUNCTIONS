"""
This program is the client side script that handles communications using my server as a dead drop.

The beauty of this setup is two-fold:
    1.) Effectively, nobody knows it exists. I don't get very much traffic.

    2.) As opposed to typical communication platforms, users log in to my server first THEN
        get served the data. Typically, the user is served data that they then log into to further interact with:
        communications are bounced from one end to another by a server in the middle.
        
        This server, however, acts less as a messenger running back and forth, but a private room in the internet 
        where no ones listening in. Data is sent letter by letter to the server via SSH; where every keystroke is 
        sent down the pipe one at a time along potentially endless different routes to reach the server.
        
        The benefits include the fact that even if somebody IS listening, they're only getting a single letter at a 
        time with no way to find the others. Drawbacks; if there's a mishap somewhere and the data doesn't get sent;
        oh well, it's gone. But, it's just a letter so really not thet big a deal for mundane communications.

"""


import socket
import threading


nickname = input("Choose a callsign: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
This line must be uncommented and populated by the user with their own
port/ip combo.

A domain is recommended, so as not to give away your security details.

    From your domain, you can point traffic to your router then 
    configure the router to forward all traffic to a dedicated host
    running this application.


#client.connect(("[HOST IP]", 'PREFERRED PORT'))

"""

def recieve():
		while True:
			try:
				message = client.recv(1024).decode('ascii')
				if message == 'NICK':
					client.send(nickname.encode('ascii'))
				else:
					print(message)

			except:
				print("Something went wrong. Try Again")
				client.close()
				break


def write():
	while True:
		message = '{}: {}'.format(nickname, input(' '))
		client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
