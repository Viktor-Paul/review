"""
共享内存实现进程间的通信
"""
from multiprocessing import Value, Array, Process
import time
from random import randint


# 1.在内存中开辟空间，进程可以进行读取和写入从而实现进程间的通信，但是每次写入会覆盖原来的值
def man(money):
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1, 1000)


def girl(money):
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100, 800)


if __name__ == "__main__":
    money = Value("i", 5000)
    p1 = Process(target=man, args=(money,))
    p2 = Process(target=girl, args=(money,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(money.value)
