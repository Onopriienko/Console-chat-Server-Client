import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('192.168.0.105', 55555))
connection_msg = '< ' + 'Ubuntu' + ' connected >'
#client_socket.sendall(str.encode(connection_msg))

while True:
    msg = input('Ch: ')
    client_socket.sendall(str.encode(msg))
    data = client_socket.recv(1024)

    # обработка информации
    print(data.decode('utf-8'))

    if not msg:
        break





