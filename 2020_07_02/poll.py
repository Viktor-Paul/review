"""
poll.py
"""
from multiprocessing import Pool
from time import sleep, ctime


def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

if __name__ == "__main__":
    # 创建对象
    pool = Pool(4)

    for i in range(10):
        msg = "hello %d" % i
        r = pool.apply_async(func=worker,args=(msg,))
        print(r.get())

    pool.close()
    pool.join()
    # print(r.get())
