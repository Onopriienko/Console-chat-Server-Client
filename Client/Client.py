import socket

sock = socket.socket()
sock.connect(('192.168.0.105', 9090))
sock.send(str.encode('hi'))

data = sock.recv(1024)
sock.close()

print (data)