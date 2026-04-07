import socket


# This variable becomes a socket object configured to use IPV4 addresses and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# These two variables configure the IP address and port that the server will listen on.
listen_on = "127.0.0.1"
port_number = 9000

# This binds the IP address and the port number to the server
server.bind((listen_on, port_number))

# This allows the server to wait for the connections, with a maximum of 5 clients in a que
server.listen(5)

# These two variables will return a private channel of server-client communication and client's IP address
private_channel, client_address = server.accept()
