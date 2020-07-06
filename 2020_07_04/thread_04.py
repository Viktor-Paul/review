"""
基于多线程的网络并发模型
server.py
"""
from socket import *
from threading import Thread
import os
import threading


def handle(c):
    print("%s 开始运行" % threading.current_thread().getName())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    print("%s 结束运行" % threading.current_thread().getName())
    c.close()


if __name__ == "__main__":
    # 创建套接字对象
    socked = socket()
    # 绑定地址
    ADDR = ("0.0.0.0", 6666)
    socked.bind(ADDR)
    # 设置监听
    socked.listen(3)

    print("listen the port ...")
    # 循环等待客户端连接
    while True:
        try:
            c, addr = socked.accept()
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = Thread(target=handle, args=(c,))
        t.setDaemon(True)
        t.start()
