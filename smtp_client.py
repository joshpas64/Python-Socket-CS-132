from socket import *
import socket
msg = "\r\n I love computer networks!" #email content
endmsg = "\r\n.\r\n"  #a single period followed by crlf indicates the 
# Choose a mail server (e.g. Google mail server) and call it mailserver
# 25 port designated for email
mailserver = ('localhost',25) ##For this protocol it is harder to test with sockets themselves
## In CS 132 we had to execute and test this file using only our UCI emails on a eecs linux machine
## that was on campus and had to be connected to remotely by ssh 
#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver) ##Create server object
#Fill in end
recv = clientSocket.recv(1024).decode() ##Remotely connect to it, the client is your local machine
print(recv) ## Receive byte message from server
if recv[:3] != '220': ##220 indicates it accepted the connection 
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n' ##HELO hostname \r\n is next command to send to server
## All messages in this protocol must terminate with \r\n
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250': ##Once again a positive acknowledgement code from the email server
 print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <jpascasc@uci.edu>\r\n' ##Sending email format MAIL FROM: <emailurl>\r\n
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode() ##250 is pos acknowledgement
if recv2[:3] != '250': ## Acknowledgement that you are a valid or safe email sender to communicate with
    print('250 reply not received from server, Sender was not deemed okay.')
print(recv2)
# Fill in end
# Send RCPT TO command and print server response.
rcpt = 'RCPT TO: <jpascasc@uci.edu>\r\n' ##Reciepient email
clientSocket.send(rcpt.encode())
recv3 = clientSocket.recv(1024).decode()
if recv3[:3] != '250': ###Acknowledgement that the email url exists on that server
    print('250 reply not received from server, Recipient was not deemed okay.')
print(recv3) ##Print response from server
# Fill in start
# Fill in end
# Send DATA command and print server response.
data = 'DATA\r\n' ##This statement indicates senders is about to send the actual email message
clientSocket.send(data.encode()) ##Send message
recv4 = clientSocket.recv(1024).decode() ##Getting receipt of 354 from server indicates it is ready to take in your message
if rev4[:3] != '354':
    print('354 server not received from server')
print(recv4)
# Fill in start
clientSocket.send(msg.encode()) ##Send message content
clientSocket.send(endmsg.encode()) ##Send end of message flag (note all the communications is done in BYTES)
quitCommand = 'QUIT\r\n'
recv6 = clientSocket.recv(1024).decode() ##Show you wish to end the connection
print(recv6)
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
clientSocket.close() ##Once it is allowed, the connection will be terminated
# Fill in end
# Send message data.
# Fill in start
# Fill in end
# Message ends with a single period.
# Fill in start
# Fill in end
# Send QUIT command and get server response.
# Fill in start
# Fill in end
