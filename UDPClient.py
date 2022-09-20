from socket import *

s_ip = 'localhost'
s_port = 12346
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)

msg = '안녕 서버야'
c_sock.sendto('안녕, server!'.encode('utf-8'), s_addr)

c_sock.close()