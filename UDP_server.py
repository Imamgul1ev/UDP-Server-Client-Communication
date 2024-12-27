import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
server.bind(ADDR)

while True:
    data, addr = server.recvfrom(PORT)
    print(str(data.decode(FORMAT)))  # Decoding the received message
    message = "Hello, I'm UDP Server!"
    server.sendto(message.encode(FORMAT), addr)  # Send response
