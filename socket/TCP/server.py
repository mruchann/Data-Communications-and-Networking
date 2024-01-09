from socket import *

serverPort = 12000
bufferSize = 1024

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, clientAddress = serverSocket.accept()

    message = connectionSocket.recv(bufferSize).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()