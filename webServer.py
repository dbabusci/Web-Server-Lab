#import socket module
from socket import *
import sys #In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#--> Fill in Start
#--> Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =#Fill in start and end
    try:
        message = #Fill in start and end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start and end
        #send one http header line into socket
        #-->Fill in start
        #-->Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print("placeholda")
        #Send response message for file not found
        #-->Fill in start
        #-->Fill in end
        #Close Client socket
        #-->Fill in start
        #-->Fill in end
serverSocket.close()
sys.exit()