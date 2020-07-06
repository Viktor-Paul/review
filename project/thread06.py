"""
client.py
"""
from socket import *

# 创建套接字对象
socked = socket()

# 绑定地址
ADDR = ("127.0.0.1", 6666)
socked.connect(ADDR)
while True:
    msg = input("msg>>")
    if not msg:
        break
    socked.send(msg.encode())
    data = socked.recv(1024)
    print(data.decode())

socked.close()
