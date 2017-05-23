import socket
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(('0.0.0.0', 55555))
print('< Server port > 55555')

clients = []


class TalkToClient(Thread):
    def __init__(self):
        Thread.__init__(self)


while True:
    data, addr = server_socket.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)

    # обработка информации
    print(data.decode('utf-8'))

    for client in clients:
        TalkToClient().start()
        if addr != client:
            server_socket.sendto(data, client)

server_socket.close()
