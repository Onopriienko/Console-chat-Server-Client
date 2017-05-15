import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 55555))
print('< Server port > 55555')

clients = []

while True:
    data, addr = server_socket.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)

    # обработка информации
    print(data.decode('utf-8'))


    for client in clients:
         # if addr != client:
        server_socket.sendto(data, client)



server_socket.close()
