from socket import *

serverPort = 12001
bufferSize = 2048

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print('The server is ready to receive!')

while True:
    message, clientAddress = serverSocket.recvfrom(bufferSize)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)