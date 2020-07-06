"""
IO多路复用之select
"""
from socket import *
from select import select

socked = socket()
socked.bind(("0.0.0.0", 8888))
socked.listen(3)

rlist = [socked]
wlist = []
xlist = [socked]

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is socked:
            c,addr = r.accept()
            print("connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                # 从关注列表移除
                rlist.remove(r)
                r.close()
                continue
            print("receive:",data.decode())
            r.send(b"ok")


    for w in ws:
        w.send(b'OK')
        wlist.remove(w)  # 使用后移除

    for x in xs:
        pass
