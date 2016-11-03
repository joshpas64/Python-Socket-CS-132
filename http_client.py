from socket import *
import sys
import socket

def run_client():
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ### usually executing a program file may be like this
        ### for Linux using a bash script it would be
        ### ./script
        ### for python its usually
        ### change to directory with the python interpreter
        ### issue python python_program.py
        ## This will run the program
        ### cmd line functions can take arguments for example in Linux
        ## ls list contents of file directories
        ### -l will list a contents access permissions
        ## so if you want to find the permissions of only the file.py in a directory
        ## issue ls -l file.py
        ## What comes after a function are called the system arguments
        ## for this program it will be run in the cmd line using
        ## python http_client IP port filepath
        args = sys.argv[1:] ##Gets all the arguments issued to it from the command line
        ## except for the first one which is just http_client and puts into a list
        port = int(args[1]) ##Retrieve port
        clientSocket.connect((args[0],port)) ##retrieve IP and connect
        ##Make a standard HTTP get request
        ##\r\n is crlf which denotes the end of all HTTP messages
        ## args[2] is webpage to retrieve
        request = "GET " + "/" + args[2] + " HTTP/1.1\r\n"
        clientSocket.send(request.encode()) ##remember they send bytes not text
        #Upon receipt of get request the server will have a response that client
        # can receive, usually denotes if the file was found, not found, moved, etc
        ##The following message from the server would usually be the data file it has requested
        ## and other metadata
        response = clientSocket.recv(2048).decode() ##Turn bytes to text
        print(response)
    except ConnectionRefusedError:
        print("I am sorry we are not able to locate the server with IP you have requested \
                 the server is unable to or has refused to connect to you.")
        print("The server may also be offline.")
    except OSError:
        print("Could not connect or make socket, use this format [IP address or hostname] [port number] [file path] \
to execute your program properly")
    except IndexError:
        print("Could not connect or make socket, use this format [IP address or hostname] [port number] [file path] \
to execute your program properly")
    except ValueError:
        print("Port number must be an integer")
    finally:
        clientSocket.close()
        
run_client()
##Note in this file we have only DEFINED THE FUNCTION SO FAR for it to work in the
## command line it must be called or executed as a statement
## thats why last line is run_client()
sys.exit() #exit cmd line


