"""
udp_server.py
"""

from socket import *

# 1.创建套接字
socket_fd = socket(AF_INET, SOCK_DGRAM)

# 2.绑定地址
ADDR = ("127.0.0.1", 8888)
socket_fd.bind(ADDR)

# 3.收发消息
while True:
    data, addr = socket_fd.recvfrom(1024)
    print("收到的消息：", data.decode())
    socket_fd.sendto(b"receive", addr)

socket_fd.close()
