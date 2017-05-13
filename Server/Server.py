import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.0.105', 5050))
print('Server > 192.168.0.105 : 5050')

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data)
conn.close()
