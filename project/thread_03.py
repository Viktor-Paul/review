"""
线程锁
"""
from threading import Thread, Lock
import time
import threading


def fun01(a, b, lock):
    lock.acquire()
    print("%s 开始启动" % threading.current_thread().getName())
    a += 1
    b += 1
    time.sleep(0.2)
    for i in range(3):
        print("a = %d ,b = %d %d" % (a, b, i,))
    print("%s 开始结束" % threading.current_thread().getName())
    lock.release()


if __name__ == "__main__":
    a = b = 0
    lock = Lock()
    t = Thread(target=fun01, args=(a, b, lock))
    t2 = Thread(target=fun01, args=(a, b, lock))
    t3 = Thread(target=fun01, args=(a, b, lock))
    t.start()
    t2.start()
    t3.start()
    t2.join()
    t3.join()
    t.join()
