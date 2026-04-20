import socket

# It determines the client's IPV and which Protocol it uses
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enter the server's IP and Port number
server_ip = "127.0.0.1"
server_port = 9000

# Connects to the server
client.connect((server_ip, server_port))

print("Connected Successfully")

message_to_client = input("Enter your message: ")

client.sendall(message_to_client.encode("utf-8"))

