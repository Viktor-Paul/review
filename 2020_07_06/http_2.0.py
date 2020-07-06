"""
http_2.0
使用select实现IO多路复用
"""
from socket import *
from select import select


class HTTPServer:
    def __init__(self, host, port, dir):
        self.address = (host, port)
        self.host = host
        self.port = port
        self.dir = dir
        self.create_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def create_socket(self):
        self.socked = socket()
        self.socked.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.socked.bind(self.address)

    def handle(self, c):
        # 接受客户端请求
        requests = c.recv(4096)
        if not requests:
            self.rlist.remove(c)
            c.close()
            return
        print(requests)
        # 提取请求
        request_line = requests.splitlines()[0]
        info = request_line.decode().split(" ")[1]
        print(c.getpeername(), ":", info)
        # info分网页和其他内容
        if info == "/" or info[-5:] == ".html":
            self.get_html(c, info)
        else:
            self.get_data(c)

    def get_html(self, connfd, info):
        if info == "/":
            filename = self.dir + "/index.html"
            print(filename)
        else:
            filename = self.dir + info
        try:
            fd = open(filename, 'r', encoding="utf-8")
        except Exception:
            # 没有找到该网页
            responseheaders = "HTTP/1.1 404 Not Found\r\n"
            responseheaders += "Content-Type:text/html\r\n"
            responseheaders += "\r\n"
            responsebody = "<h1>sorry,Not found the page</h1>"
            response = responseheaders + responsebody
            connfd.send(response.encode())
        else:
            responseheaders = "HTTP/1.1 200 OK\r\n"
            responseheaders += "Content-Type:text/html\r\n"
            responseheaders += "\r\n"
            responsebody = fd.read()
            response = responseheaders + responsebody
            connfd.send(response.encode())

    def get_data(self, connfd):
        responseheaders = "HTTP/1.1 200 OK\r\n"
        responseheaders += "Content-Type:text/html\r\n"
        responseheaders += "\r\n"
        responsebody = "<h1>waiting for httpserver 3.0</h1>"
        response = responseheaders + responsebody
        connfd.send(response.encode())

    def server_forever(self):
        self.socked.listen(5)
        print("listen the port %d" % self.port)
        self.rlist.append(self.socked)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.socked:
                    conned, addr = r.accept()
                    print("connect from:", addr)
                    self.rlist.append(conned)
                else:
                    self.handle(r)

            for w in ws:
                pass
            for x in xs:
                pass


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8000
    # 网页存储位置
    DIR = "E:/python/review_2020_07/2020_07_06/static"
    httppd = HTTPServer(HOST, PORT, DIR)
    httppd.server_forever()
