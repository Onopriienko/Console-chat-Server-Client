import socket
import sys
import select

HOST = '127.0.0.1'
PORT = 7878


def close_chat():
    print('\nDisconnected from chat server')
    client_socket.close()
    sys.exit()

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
except socket.error:
    print('Failed to create socket.')
    close_chat()

try:
    client_socket.connect((HOST, PORT))
except socket.error:
    print('Connection to server failed')
    close_chat()

name = input('Enter your name: ')
print('Connected to remote host. You can start sending messages', '\n')
sys.stdout.write('Me: ')
sys.stdout.flush()


while True:
    socket_list = [sys.stdin, client_socket]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == client_socket:
            data = sock.recv(4096)
            if not data:
                close_chat()
            else:
                sys.stdout.write(data.decode('utf-8'))
                sys.stdout.write('Me: ')
                sys.stdout.flush()
        else:
            msg = sys.stdin.readline()
            if msg.strip('\n') in ['q', 'quit', 'exit']:
                close_chat()
            else:
                try:
                    client_socket.send(name.encode('utf-8') + b': ' + msg.encode('utf-8'))
                    sys.stdout.write('Me: ')
                    sys.stdout.flush()
                except socket.error:
                    print('Send failed')
                    close_chat()
