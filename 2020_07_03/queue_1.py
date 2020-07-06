"""
使用队列实现进程间的通信
在父进程中创建两个子进程，其中一个负责写数据，一个负责读数据
"""
from multiprocessing import Queue, Process
from time import sleep
import random


# 读数据
def fun01(q):
    while True:
        if not q.empty():
            print(q.get(True))
            sleep(random.random())
        else:
            break


def fun02(q):
    for i in range(10):
        if not q.full():
            q.put("消息%d" % i)
            sleep(random.random())


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=fun02, args=(q,))
    p3 = Process(target=fun02, args=(q,))
    p2 = Process(target=fun01, args=(q,))
    p1.start()
    p3.start()
    p2.start()
    p1.join()
    p3.join()
    p2.join()
