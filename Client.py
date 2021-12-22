import socket

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888

ClientSocket.connect((host, port))
data = ['SYN', 'ACK']

def clientSend():
    while True:
        message = input('Client: ')
        ClientSocket.send(message.encode('utf-8'))
        if data[1] == 'SYN':
            clientReceive()
        else:
            ClientSocket.close()

def clientReceive():
        dataFromServer = ClientSocket.recv(1024)
        print('Data received: {}'.format(dataFromServer.decode()))

        dataFromServer = ClientSocket.recv(1024)
        print('Data received: {}'.format(dataFromServer.decode()))



