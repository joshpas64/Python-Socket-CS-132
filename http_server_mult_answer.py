# Import socket module
from socket import *
import _thread

# celintService function gets client address and client socket as inputs
# then reads the data from client socket and process the request
# in multi thread programming, each thread call this function when it is created
def clientService(clientAdd, clientSocket):
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
                # Receives the request message from the client
                message =  clientSocket.recv(1024)

                # Extract the path of the requested object from the message
                # The path is the second part of HTTP header, identified by [1]
                filename = message.split()[1]

                # Because the extracted path of the HTTP request includes
                # a character '\', we read the path from the second character
                f = open(filename[1:], "rb")

                # Store the entire contenet of the requested file in a temporary buffer
                outputdata = f.read()
                f.close()

                # Send the HTTP response header line to the connection socket
                clientSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

                # Send the content of the requested file to the connection socket
                for i in range(0, len(outputdata)):
                    clientSocket.send(outputdata[i:i+1])
                clientSocket.send(b'\r\n')


        except IOError:
                # Send HTTP response message for file not found
                clientSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
                clientSocket.send(b'<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')

        # Close the client connection socket
        clientSocket.close()


# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6788

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 10 connection at a time
serverSocket.listen(10)

# Server should be up and running and listening to the incoming connections
while True:
	print ('Ready to serve...')
	# Set up a new connection from the client
	connectionSocket, clientAddr = serverSocket.accept()
        # create a new thread to service a client by calling clientService inside the new thread
	# pass connection socket and client address into this thread to use when it calls function
	_thread.start_new_thread(clientService, (clientAddr, connectionSocket))

serverSocket.close()
