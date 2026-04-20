import socket
from encodings import utf_8

# This variable becomes a socket object configured to use IPV4 addresses and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# These two variables configure the IP address and port that the server will listen on.
listen_on = "127.0.0.1"
port_number = 9000

# Show that the server is listening on what ip and port number
print(f"Server listening on IP: {listen_on} Port: {port_number}")

# This binds the IP address and the port number to the server
server.bind((listen_on, port_number))

# This allows the server to wait for the connections, with a maximum of 5 clients in a que
server.listen(5)

# private_channel returns a private channel and client_address returns client's IP address
private_channel, client_address = server.accept()


# Show that the use connected to the server using its IP address
print(f"Client Connected: {client_address}")

# Enables the server to receive data
data = private_channel.recv(1024)

# Decodes the message from the client
message = data.decode("utf_8")

print(f"Client's message: {message}")
