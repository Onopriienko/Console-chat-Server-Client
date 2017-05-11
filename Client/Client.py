import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
sock.send(str.encode('hi'))

data = sock.recv(1024)
data = bytes.decode(data)
sock.close()

print(data)