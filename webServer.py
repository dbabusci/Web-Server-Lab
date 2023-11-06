from socket import *
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("10.5.1.146", 8000))
serverSocket.listen(5)
print("before true")
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        print("in try")
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')#expects bits not string
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        print("File not found")
        connectionSocket.close()
serverSocket.close()
sys.exit()