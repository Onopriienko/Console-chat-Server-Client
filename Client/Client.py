import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client_socket.connect(('127.0.0.1', 55555))
name = input('Enter your name: ')
connection_msg = '< ' + name + ' connected >'
client_socket.sendall(str.encode(connection_msg))



while True:
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))
    msg = input(name + ': ')
    client_socket.sendall(str.encode(name) + b': ' + str.encode(msg))

    # обработка информации
    # print(data.decode('utf-8'))

    if not msg or msg == 'bye':
        break


client_socket.close()




