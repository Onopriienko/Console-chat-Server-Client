import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen(10)
print('< Server port > 55555')

SOCKET_LIST = []
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
        print('a',ready_to_read)
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            print('b',addr)
            SOCKET_LIST.append(sockfd)
            print("Client (%s, %s) connected" % addr)
            broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
        else:
            try:
                data = sock.recv(4096)
                if data:
                    broadcast(server_socket, sock, data.decode('utf-8'))
                else:
                    if sock in SOCKET_LIST:
                        SOCKET_LIST.remove(sock)
                    broadcast(server_socket, sock, "fClient (%s, %s) is offline\n" % addr)
            except:
                 broadcast(server_socket, sock, "gClient (%s, %s) is offline\n" % addr)
                 continue


server_socket.close()




