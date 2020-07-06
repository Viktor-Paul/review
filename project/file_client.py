"""
client.py
"""
from socket import *
import time

# 创建套接字对象
socked = socket()

# 绑定地址
ADDR = ("127.0.0.1", 8800)
socked.connect(ADDR)


def menu():
    print("\n=========命令选项==========")
    print("****      list         ****")
    print("****    get file       ****")
    print("****    put file       ****")
    print("****      quit         ****")
    print("=============================")


def show_list(socked):
    # 发送请求
    socked.send(b"L")
    # 等待回复
    data = socked.recv(1024)
    if not data:
        return
    if data == b"ok":
        data = socked.recv(1024)
        list01 = data.decode().split('\n')[:-1]
        print(list01)
    else:
        print(data.decode())


def download_file(socked, filename):
    # 发送请求
    socked.send(b"G " + filename.encode())
    # 等待回复
    data = socked.recv(1024)
    if data == b"ok":
        fd = open(filename, "wb")
        while True:
            # 接受文件
            data = socked.recv(1024)
            if data == b"##":
                break
            fd.write(data)
        fd.close()
    else:
        print(data.decode())


def upload_file(socked, filename):
    try:
        fd = open(filename, "rb")
    except:
        print("文件不存在")
        return
    # 发送请求
    socked.send(b"P " + filename.encode())
    # 等待回复
    data = socked.recv(1024)
    if data == b"ok":
        # 传送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                socked.send(b"##")
                break
            socked.send(data)
        fd.close()
    else:
        print(data.decode())


def handle_quit(socked):
    socked.send(b"Q")
    data = socked.recv(1024)
    if data == b"ok":
        print("客户端退出")
        return "quit"


while True:
    menu()
    msg = input("请输入命令：")
    if msg == "list":
        # 查看列表
        show_list(socked)
    elif msg[:3] == "get":
        # 下载文件
        filename = msg.strip().split(" ")[1]
        download_file(socked, filename)
    elif msg[:3] == "put":
        # 上传列表
        filename = msg.strip().split(" ")[1]
        upload_file(socked, filename)
    elif msg == "quit":
        # 退出
        result = handle_quit(socked)
        if result == "quit":
            break
    else:
        print("请输入正确的命令")

socked.close()
