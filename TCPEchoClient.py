from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(s_addr)

while True:
    inputData = input('입력 문자열 : ')
    c_sock.send(inputData.encode('utf-8'))
    print(c_sock.recv(1024).decode('utf-8'))

    