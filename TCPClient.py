from socket import *

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect( (s_ip, s_port) )

data1 = 'Received data from server : '
print(data1, c_sock.recv(1024).decode('utf-8'))
data2 = 'Hello, TCP Server'
c_sock.send(data2.encode('utf-8'))

c_sock.close()