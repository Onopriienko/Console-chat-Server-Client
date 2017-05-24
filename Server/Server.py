import socket
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(('0.0.0.0', 55566))
server_socket.listen(10)
print('< Server port > 55555')

clients = []
#recvData = []


class TalkToClient(Thread):
    def __init__(self, client_sock, client_addr):
        Thread.__init__(self)
        self.client_sock = client_sock
        self.client_addr = client_addr
        print(self.client_addr)

    def run(self):
        while True:
            rec_data = self.client_sock.recv(1024)
            for n in clients:
                #print(n)
                if n != self.client_addr:
                    print(n)
                    print(self.client_addr)
                    self.client_sock.sendto(rec_data, n)
            '''
            if not rec_data:
                self.client_sock.send(b'bye')
                break
            print(rec_data)
            for client in clients:
                self.client_sock.sendto(rec_data, client)
            '''



while True:
    sock, addr = server_socket.accept()

    if addr not in clients:
        clients.append(addr)
    #print(sock)
    #print(addr)
    #print(clients)

    #for client in clients:
        #print(client, b'<')
    TalkToClient(sock, addr).start()
        #sock.sendto(rec_data, clients)
        #if addr != client:
        #server_socket.sendto(data, client)

server_socket.close()
