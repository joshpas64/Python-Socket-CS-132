#import socket module
## GET localdir/local.html HTTP/1.1
## localhost (IP)
## connection: close
## user-agent: browser (might test with internet explorer too

from socket import *
import sys # In order to terminate the program
import socket
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
uciIp = "169.234.47.210"
homewifiip = "2602:306:bccc:d5a0:edd2:3862:a24f:8e5a"
adapterip = "192.168.56.1"
localIp = socket.gethostbyname(socket.gethostname())
port = 6789
#Prepare a server socket
#Fill in start
serverSocket.bind(('',port))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    s = serverSocket.getsockname()
    print(s)
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    a = "Connection taken from " + str(addr[0])
    print(a)
    try:
         message = connectionSocket.recv(2048)#Fill in start #Fill in end
         filename = message.split()[1]
         f = open(filename[1:],'rb')
         outputdata = f.readlines()#Fill in start #Fill in end
         #Send one HTTP header line into socket
         #Fill in start
         connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
         #Fill in end
         #Send the content of the requested file to the client
         for i in range(0, len(outputdata)):
             connectionSocket.send(outputdata[i])
         connectionSocket.send("\r\n".encode())
         f.close()
         connectionSocket.close()
    except IOError:
    #Send response message for file not found
        connectionSocket.send("<html><head><title> 404 Not Found 1</title></head><body><h1>404 Error</h1><p> The page you requested was not found</p></body></html>\
        \r\n".encode())
        #Fill in start 
        #Fill in end
        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
