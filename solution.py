from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Assignment3"
    endmsg = "\r\n.\r\n"


    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope


    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #print recv
    #if recv[:3] != '220':
       #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice \r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailfromCommand = 'MAIL FROM: <mp6296@nyu.edu> \r\n'
    clientSocket.send(mailfromCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcpttoCommand = 'RCPT TO: <mr6296@nyu.edu> \r\n'
    clientSocket.send(mailfromCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send DATA command and handle server response.
    dataCommand = 'Data\r\n'
    clientSocket.send(dataCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send message data
    clientSocket.send(msg.encode)

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    quitCommand = 'Quit\r\n'
    clientSocket.send(quitCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')