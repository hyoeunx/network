from http import client
from pydoc import cli
from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s_sock.bind(s_addr)
s_sock.listen(2)

client, c_addr = s_sock.accept()
print(c_addr, 'Now Connected')

data = 'dummy'
while len(data):
    data = client.recv(1024).decode('utf-8')

    if data=='q':
        print('\n수신종료')
        break

    print('수신된 Data : ', data)
    client.send(data.encode('utf-8'))


client.close()
s_sock.close()