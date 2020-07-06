"""
线程
"""
from threading import Thread,Lock
import time
import os


def music(a,lock):
    lock.acquire()
    for i in range(3):
        time.sleep(0.1)
        print(os.getpid(), "播放一路平安")
    print("a = ", a)
    # global a
    a = 1000
    print("a : ", a)
    lock.release()


def sport(a,lock):
    lock.acquire()
    for i in range(3):
        time.sleep(0.1)
        print(os.getpid(), "正在拍球")

    print("a = ", a)
    # global a
    a = 100
    print("a : ", a)
    lock.release()


if __name__ == "__main__":
    # 创建线程对象
    a = 1
    lock = Lock()

    t = Thread(target=music, args=(a,lock))
    t2 = Thread(target=music, args=(a,lock))
    t3 = Thread(target=sport, args=(a,lock))
    t4 = Thread(target=sport, args=(a,lock))
    for i in range(4):
        time.sleep(1)
        print(os.getpid(), "播放葫芦娃")
    t.start()
    t2.start()
    t3.start()
    t4.start()
    t4.join()
    t.join()
    t2.join()
    t3.join()
    print("main a", a)
