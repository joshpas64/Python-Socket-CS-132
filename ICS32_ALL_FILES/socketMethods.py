###Joshua Pascascio ID: 52192782
### Heran Patel: 62984531

import socket
from collections import namedtuple
socketSet = namedtuple('socketSet',['socket','socket_in','socket_out'])

def read_port() -> int:
    """Server finding method for an online interface, takes only integers in the range
    and returns an int to use a port number to make a connection"""
    while True:
        try:
            port = int(input("Enter a port number:  ").strip())
            if port < 0 or port > 65535:
                print("Port must be in range of 0 to 65535")
            else: 
                return port

        except ValueError:
            print("Port must be an integer")
def get_host() -> str:
    """Take a string as input and will use it as a host name, can be IP address or URL"""
    while True:
        host = input("Please enter a host(host name or IP address is acceptable):  ")
        if host == "":
            print("Give me a host")
        else: 
            return host
def establish_connection() -> socketSet:
    """Method that takes input and uses it to make a server connection as well as socket objects for reading and
    writing in the form of socketSet"""
    host = get_host()
    port = read_port()
    connection_set = host, port
    main_socket = socket.socket()
    socket_input = main_socket.makefile('r')
    socket_output = main_socket.makefile('w')
    main_socket.connect(connection_set)
    socketStructure = socketSet(main_socket,socket_input,socket_output)
    return socketStructure


def send_message(socketStructure: socketSet, message: str) -> None:
    """Abstracted simpler way of writing to a socket or server with the socketSet namedTuple object"""
    socketStructure.socket_out.write(message + "\r\n")
    socketStructure.socket_out.flush()
def recv_message(socketStructure: socketSet) -> str:
    """Abstracted way reading input or the output from a socket object thrrough the use socketSet namedTuple object"""
    return socketStructure.socket_in.readline()[:-1]
def close(socketStructure: socketSet) -> None:
    """Closes the connections made by the socketSet's input and output fields"""
    socketStructure.socket.close()
    socketStructure.socket_in.close()
    socketStructure.socket_out.close()
