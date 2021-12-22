import socket

host = socket.gethostname()
port = 8888

#membuat socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((host,port))
ServerSocket.listen()
print('Server is running')
client, address = ServerSocket.accept()
print('Connected with: ' + str(address))


def receive(client):
    while True:
        try:
            clientData = client.recv(1024)
            print('Client: {}'.format(clientData.decode()))
            send(clientData)

        except:
            #remove client that is not related anymore
            client.close()


def send(data): #send data to client
    client.send(data)
    client.send(data)
    clientData = client.recv(1024)
    print('Client: {}'.format(clientData.decode()))




