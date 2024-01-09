from socket import *

serverName = gethostname()
bufferSize = 1024

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence: ')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(bufferSize)

print('From Server: ', modifiedMessage.decode())
clientSocket.close()