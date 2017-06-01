import socket
import select
import sys

HOST = '0.0.0.0'
PORT = 7878
MAXCLIENT = 20
SOCKET_LIST = []


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
except socket.error:
    print('Failed to create socket.')
    sys.exit()

try:
    server_socket.bind((HOST, PORT))
except socket.error:
    print('Bind failed.')
    sys.exit()

server_socket.listen(MAXCLIENT)
print('< Server port > ', PORT)

SOCKET_LIST.append(server_socket)


def broadcast(server_socket, sock, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message.encode('utf-8'))
            except:
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

while True:
    ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)
    for sock in ready_to_read:
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            SOCKET_LIST.append(sockfd)
            print("Client (%s, %s) connected" % addr)
            broadcast(server_socket, sockfd, '\r' + "[%s:%s] entered our chatting room\n" % addr)
        else:
            try:
                data = sock.recv(4096)
                if data:
                    broadcast(server_socket, sock, '\r' + data.decode('utf-8'))
                else:
                    if sock in SOCKET_LIST:
                        SOCKET_LIST.remove(sock)
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
            except:
                 broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                 continue

server_socket.close()
