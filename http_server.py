#import socket module
## GET localdir/local.html HTTP/1.1
## localhost (IP)
## connection: close
## user-agent: browser (might test with internet explorer too

from socket import *
import sys # In order to terminate the program
import socket #socket
#A socket is an application interface between computer processes communicate
#and exchange data
#This all done through the socket object itself
#When it is initialized it can be given certain values such as what protocol
#like TCP or UDP
#Whether you can reuse address, ports, etc
##Look at python 3.5 Documentation for more details on constant
## SOCK_STREAM: TCP protocol
## socket can be initialized as a connection between two computers
## Can also be setup as a listening server and even forward connections for other
## Services
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
port = 6789
#Prepare a server socket
#Fill in start
serverSocket.bind(('',port))
##This socket will use the most convenient IP address on the computer is processing
## most likely localhost and use port 6789
##IP Address: The address of your computer on the internet that others can connect to
## Port space reserved for certain processes (i.e. port 80 is web HTTP 25 is for email SMTP communicatioN)

serverSocket.listen(1)
##Listen for only one connection 
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    ##Make a new socket that represents the connection between client and server
    print(addr)
    try:
         message = connectionSocket.recv(2048) ##Receive up to 2048 bytes from client
         ## Since it connected to server as TCP HTTP it will likely be an HTTP request in
         ## Format: (BASIC) "GET /pathtothewebpage HTTP/1.1 \r\n\r\n"
         ## Note this message is not sent in text but in bytes so must encode like this
         ## send(b"TEXTMESSAGE")
         ## send("TEXT".encode())
         print(connectionSocket.getpeername())#Fill in start #Fill in end
         ### GETs the remote socket's information usually its a tuple in form
         ## (IP,port)
         filename = message.split()[1]
         ##.split splits a string into a list by making the character in the parameter
         ## denote different items
         ## i.e. "BBBACCCADDDD".split("A") = ["BBB","CCC","DDD"]
         ## if no params are given a space is assumed to be that character
         ## This will take out the GET and get the file path
         f = open(filename[1:],'rb') #take file path and read it as byte objects
         ## reading as byte objects is easier when there are references to images or other
         ## non text objects
         outputdata = f.read()#Fill in start #Fill in end
         #Send one HTTP header line into socket
         #Fill in start
         connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
         ##For client to be able receive data from server it must get an OK from it
         ## that code is 200 OK
         ## Send that message to the client
         #Fill in end
         #Send the content of the requested file to the client
         for i in range(0, len(outputdata)):
             connectionSocket.send(outputdata[i:i+1]) ##send data to client byte by byte
         ## If the document you're sending has object references like pictures
         ## For safe measure make sure they are in the same directory the server (the python code)
         ## Also some browser may not load images sometime so perhaps with images go to source code and
         ## for an image do this <img src="imagepath.png" alt="someimage">
         ## If browser compatibility prevents image display, the text in the alt field will be displayed
         ## This means your server code works such that no byte or encode errors were thrown
         connectionSocket.send("\r\n\r\n".encode()) ## This denotes the end of the HTTP message
         ##HTTP Response format
         ##"HTTP/version_number number_code number_word crlf" followed with data
         ## data ended with crlf
         ##Most full HTTP messages always end with something called CLRLF:
         ## carriage return line feed
         ## In Python this is \r\n\r\n
         f.close()
         connectionSocket.close() ##Done close file and TCP connections
    except IOError:
    #Send response message for file not found
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n') ##Send a 404 Error to client
        connectionSocket.send("<html><head><title> 404 Not Found 1</title></head><body><h1>404 Error</h1><p> The page you requested was not found</p></body></html>\r\n".encode())
        ### Send a standard 404 webpage document
        ### You can use html tags in sending data but remember to encode them, also some references may not
        ### work on certain browsers
        #Fill in start 
        #Fill in end
        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end
serverSocket.close() ##close sockets
sys.exit()#Terminate the program after sending the corresponding data ##This will close command line or terminal if it is used to run this program
