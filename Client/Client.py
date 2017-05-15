import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('127.0.0.1', 55555))
name = input('Enter your name: ')
connection_msg = '< ' + name + ' connected >'
client_socket.sendall(str.encode(connection_msg))



while True:
    msg = input(name + ': ')
    client_socket.sendall(str.encode(name) + b': ' + str.encode(msg))
    data = client_socket.recv(1024)

    # обработка информации
    print(data.decode('utf-8'))

    if not msg:
        break

client_socket.close()




