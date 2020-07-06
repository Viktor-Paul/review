"""
协程
优点：使用的是子程序处理IO密集型程序，而不是线程，没有线程切换的开销，由程序自身进行切换
"""
import gevent
import requests
from gevent import monkey

monkey.patch_all()


def get_body(i):
    print(f"start-{i}")
    requests.get("https://www.baidu.com").content.decode()
    print(f"end-{i}")


tasks = [gevent.spawn(get_body, i) for i in range(3)]
gevent.joinall(tasks)
