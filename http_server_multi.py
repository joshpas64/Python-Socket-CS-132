import threading
from socket import *
import socket
import sys
##Proxy Server??
## sockopt -- REUSEADR SOL_SOCKET
## A thread is an object used for parallel and synchronous and asynchronous processing
## To make use class(threading.Thread) <- Objects put in parentheses denote inheritance
## When to determine what it does you must override its .run() method
## You can make threads, wait, have them locked, be joined together, etc
## To start a thread do mythread.start() which will then call
## the.run() you override in your thread class
main_port = 6789 ##Listening port
class socketThread(threading.Thread):
    def __init__(self,name, addr, forwardSocket,newIP,newport):
        print(socket.gethostbyname(newIP))
        threading.Thread.__init__(self) ##Make a new thread
        self.name = name ##Give it a name
        self.proxy = addr ##take a socket connected to the host
        self.port = newport ## take the proxy that will forward the connection
        self.IP = newIP ##Service server's IP
        self.servSock = forwardSocket ##Service server's port
        self.servSock.connect((self.IP,self.port)) ##Connected to the new port
    def run(self):
        ##make a new connection with server port using connect and ID attribute
        ##does the threading class need a socket attribute variable
            #Establish the connection
        print('Ready to serve...')
        #Fill in start #Fill in end
        connectionSocket = self.proxy ##Initialize connection
        while True:
            try:
                 message = connectionSocket.recv(2048) ## Get the HTTP request from client
                 self.servSock.send(message)#Send it to new server
                 filename = message.split()[1] ##Same as original web server
                 f = open(filename[1:],'rb')
                 outputdata = f.read()#Fill in start #Fill in end
                 #Send one HTTP header line into socket
                 #Fill in start
                 connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n".encode())
                 #Fill in end
                 #Send the content of the requested file to the client
                 for i in range(0, len(outputdata)):
                     a = outputdata[i:i+1]
                     connectionSocket.send(a)
                 connectionSocket.send("\r\n\r\n".encode())
                 f.close()
                 self.proxy.close()
                 self.servSock.close()
                 connectionSocket.close() #Close Connections
                 
            except IOError:
            #Send response message for file not found
                print("HMMM") ##Same as original web server
                connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
                connectionSocket.send("<html><head><title> 404 Not Found 1</title></head><body><h1>404 Error</h1><p> The page you requested was not found</p></body></html>\r\n".encode())
                #Fill in start 
                #Fill in end
                #Close client socket
                self.proxy.close()
                self.servSock.close()
                connectionSocket.close()
                #Fill in start
                #Fill in end
serverSocket = socket.socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',main_port))  ##This will proxy/listening server
serverSocket.listen(5)
newIP  = socket.gethostbyname(serverSocket.getsockname()[0]) ##Get server's IP address in number form, not domain name
###If you are going to use ports on your local machine for TCP connections
### Use command line with the IP you wish to use
### IP's on your local machine can be your offline IP (localhost), the IP address used
### to find your computer on your internet plan, other applications that may run that use their own IP
### An example is my Linux VM which has a different mainPC and localhost IP
### than my actual OS running Windows 10

#### If you are going to connect to another socket make sure it is on a socket that
## is on a port available for listening
#### On DOS to find those ports on your local machine issue
#####   netstat -an
#### 0.0.0.0 , 127.0.0.1 can be used to denote localhost
#### Format IPaddr:port
#### For whatever IP addresss youre using as the other server, go and check to make sure it is TCP and is Listening mode
ports = [5354,8307]
## These are two ports on my localhost machine that are still available to be used for connections
x = 0
while x < 2: ##Use new port in the available port list when starting a new thread
    ## Note this will work fine but it can run out of ports very quickly leaving socket not existing errors
    ## since there is no port left for socket to connect to #Check official answer for better implementation
    connectionSocket, addr = serverSocket.accept()
    ## When a listening server accepts a connection it will return
    ## a socket object connecting the two, and a tuple denoting
    ## the (ip,port) of the client
    s = socket.socket(AF_INET,SOCK_STREAM) ##Create a new socket and start the thread
    print(ports[x])
    socketThread('Thread',connectionSocket,s,newIP,ports[x]).start()
    x+=1
serverSocket.close()
sys.exit() ##exit
