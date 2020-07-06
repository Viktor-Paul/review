"""
共享内存array
"""
from multiprocessing import Array, Process
from time import sleep


def fun(shm):
    sleep(2)
    # 共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = b'H'


def fun02(shm):
    for i in shm:
        print(i)
    shm[1] = b"N"


if __name__ == "__main__":
    # shm = Array("i", [1, 2, 3])
    shm = Array('c', 'hello'.encode())
    p = Process(target=fun, args=(shm,))
    p2 = Process(target=fun02, args=(shm,))
    p.start()
    p2.start()
    p.join()
    p2.join()
    for i in shm:
        print(i)
    print(shm.value)
