import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
sock.bind(('127.0.0.1', 9090))
sock.listen(5)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data)
conn.close()
