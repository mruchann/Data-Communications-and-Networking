from socket import *

serverName = gethostname()
serverPort = 12001
bufferSize = 2048

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)

print(modifiedMessage.decode())

clientSocket.close()