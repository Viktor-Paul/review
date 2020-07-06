"""
功能
【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
【2】 客户端可以查看服务器文件库中有什么文件。
【3】 客户端可以从文件库中下载文件到本地。
【4】 客户端可以上传一个本地文件到文件库。
【5】 使用print在客户端打印命令输入提示，引导操作
"""
from socket import *
from threading import Thread
import time
import os

FTP = "E:/python/review_2020_07/2020_07_04/"


def do_list(conned, addr):
    # 获取文件列表
    list01 = os.listdir(FTP)
    if not list01:
        conned.send("文件库为空".encode())
        return
    else:
        conned.send(b"ok")
        time.sleep(0.1)
        # 拼接文件列表
        files = ""
        for i in list01:
            files += i + "\n"
        conned.send(files.encode())


def do_quit(conned):
    time.sleep(0.2)
    conned.send(b"ok")
    return "quit"


def do_get(conned, filename):
    try:
        file = FTP + filename
        print(file)
        fd = open(file, "rb")
    except Exception as e:
        conned.send("文件不存在".encode())
        # conned.close()
    else:
        conned.send(b"ok")
        time.sleep(0.1)
        while True:
            # 文件发送
            data = fd.read(1024)
            time.sleep(0.2)
            if not data:
                time.sleep(0.1)
                conned.send(b"##")
                break
            conned.send(data)

        # conned.close()


def do_put(conned, filename):
    if os.path.exists(FTP + filename):
        conned.send("文件已存在".encode())
        # conned.close()
        return
    conned.send(b"ok")
    # 接受文件
    fd = open(FTP + filename, "wb")
    while True:
        data = conned.recv(1024)
        if data == b"##":
            break
        fd.write(data)
    fd.close()
    # conned.close()


def handle(conned, addr):
    while True:
        data = conned.recv(1024).decode()
        if not data:
            break
        print("%d :" % addr[1], data)
        print("data.split(" ")[0]", data.split(" ")[0])
        if data == "Q" or not data:
            result = do_quit(conned)
            if result == "quit":
                break
        elif data == "L":
            do_list(conned, addr)
        elif data.split(" ")[0] == "G":
            filename = data.split(" ")[1]
            do_get(conned, filename)
        elif data.split(" ")[0] == "P":
            filename = data.split(" ")[1]
            do_put(conned, filename)
    conned.close()


if __name__ == "__main__":
    # 创建套接字
    socked = socket(AF_INET, SOCK_STREAM)
    # 设置地址
    HOST = "0.0.0.0"
    PORT = 8800
    ADDR = (HOST, PORT)

    # 绑定地址
    socked.bind(ADDR)

    # 设置监听
    socked.listen(3)

    # 循环等待接受客户端的请求
    while True:
        # print("wait for connect ...")
        conned, addr = socked.accept()
        print("connect the addr %d" % addr[1])
        # 创建线程处理客户端请求
        t = Thread(target=handle, args=(conned, addr))
        # t.setDaemon(True)
        t.start()
        t.join()
        conned.close()
