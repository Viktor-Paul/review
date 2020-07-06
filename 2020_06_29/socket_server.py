"""
tcp_server.py
"""
import socket

# 1.创建套接字
sock_fd = socket.socket()
print(sock_fd)

# 2.绑定地址
sock_fd.bind(('127.0.0.1', 8888))

# 3.设置监听
sock_fd.listen(3)

# 4.等待处理客户端连接请求
while True:
    print("waiting for connect ...")
    conn_fd, address = sock_fd.accept()
    print("connect from", address)
    # 接受消息
    while True:
        data = conn_fd.recv(1024)
        if not data:
            break
        print("message:", data.decode())
        n = conn_fd.send(b"thanks you")
        print(n)
    conn_fd.close()


# 5.关闭套接字
# n = conn_fd.send("hello_world")

sock_fd.close()
