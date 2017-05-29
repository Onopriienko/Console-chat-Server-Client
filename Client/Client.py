import socket
import sys
import select

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.connect(('127.0.0.1', 5555))
name = input('Enter your name: ')
#client_socket.settimeout(2)

print('Connected to remote host. You can start sending messages')
print(name + ': ')

while True:
    socket_list = [sys.stdin, client_socket]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == client_socket:
            data = sock.recv(4096)
            if not data:
                print('\nDisconnected from chat server')
                sys.exit()
            else:
                print(data.decode('utf-8'))
                print(name, ': ')
        else:
            msg = sys.stdin.readline()
            client_socket.send(name.encode('utf-8') + b': ' + msg.encode('utf-8'))
            print(name, ': ')
