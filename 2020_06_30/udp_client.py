"""
udp_client.py
"""

from socket import *

ADDR = ("127.0.0.1", 8888)
# 1.创建套接字
socket_fd = socket(AF_INET, SOCK_DGRAM)

# 2.收发消息
while True:
    message = input("mess>>")
    socket_fd.sendto(message.encode(), ADDR)
    mess, addr = socket_fd.recvfrom(1024)
    print("from server:", mess.decode())
# 3.关闭套接字
socket_fd.close()
