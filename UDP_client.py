import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
msg = "Hello UDP Server"
client.sendto(msg.encode(FORMAT), ADDR)

data, addr = client.recvfrom(4096)
print("Server Says:")
print(str(data.decode(FORMAT)))  # Decoding the received message
client.close()
