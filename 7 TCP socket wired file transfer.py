# server.py
import  socket
import os


def send_file(filename,socket_):
    if os.path.exists(filename):
        socket_.send(f'Sending {filename} of size {os.path.getsize(filename)}'.encode())
        with open(filename,'rb') as f:
            bytes_to_send = f.read(1024)
            while bytes_to_send:
                socket_.send(bytes_to_send)
                bytes_to_send = f.read(1024)
        print(f"{filename} sent successfully")
    else:
        socket_.send('File does not exist '.encode())



def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1',9787))

    server.listen(1)
    print("Listening")

    communication_socket,address = server.accept()
    print(f"Connected to {address}")

    filename = communication_socket.recv(1024).decode("utf8")
    print(f"Client requesting : {filename}")

    send_file(filename,communication_socket)


main()




#clisent.py
import socket   

def receive_file(filename,socket_):
    message = socket_.recv(1024).decode('utf-8')
    print(message)
    filesize = float(message.split(' ')[-1])
    with open(filename, 'ab') as f:
        bytes_received = socket_.recv(1024)
        total_received = len(bytes_received)

        while total_received < filesize:
            bytes_received = socket_.recv(1024)
            total_received += len(bytes_received)
            f.write(bytes_received)

    print('File received')

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',9787))

    filename = input('Enter filename:')
    client.send(filename.encode())
    
    receive_file(filename,client)
    client.close()

main()
