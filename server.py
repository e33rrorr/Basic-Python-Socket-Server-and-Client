import socket
from encodings import utf_8

# This variable becomes a socket object configured to use IPV4 addresses and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Enter the IP address that the machine has
enter_ip = input("Enter the IP for the server to listen on: ")
enter_port = int(input("Enter the port number for the server: "))


# Show that the server is listening on what ip and port number
print(f"Server listening on IP: {enter_ip} Port: {enter_port}")

# This binds the IP address and the port number to the server
server.bind((enter_ip, enter_port))


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
