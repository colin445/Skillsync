import socket
client = socket.socket(socket.Af_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

message = client.recv(1024).decode()
client.send(input(message),encode())
message = client.recv(1024).decode()
client.send(input(message),encode())
print(client.recv(1024).decode())