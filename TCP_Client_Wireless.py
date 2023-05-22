# TCP client side

from socket import *

# server setting
serverName = '192.168.214.181'
serverPort = 12000

# create a client socket and initiate a TC connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Get user data and send data to the server
sentence = input("Input lower case data: ")
clientSocket.send(sentence.encode())

# receive data form server and print the result
modifiedSentence = clientSocket.recv(1024)
print('Received data from Server: ', modifiedSentence.decode())
clientSocket.close()



