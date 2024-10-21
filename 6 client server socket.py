# server.py
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9082))

server.listen(2)
print('Listening.......')
while True:
    communication_socket, ip_address = server.accept()
    print(f'Connected to {ip_address}')

    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from Client: {message}')

    communication_socket.send('Server received your message'.encode())
    communication_socket.close()

    print(f'Connection with {ip_address} ended')


# client.py
import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('127.0.0.1',9082))

socket.send('Hello There!'.encode())
message =socket.recv(1024).decode('utf-8')
print(message)
