import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('192.168.0.105', 5050))
connection_msg = '< ' + 'Ubuntu' + ' connected >'
client_socket.sendall(str.encode(connection_msg))

data = client_socket.recv(1024)
data = bytes.decode(data)
client_socket.close()

print(data)
