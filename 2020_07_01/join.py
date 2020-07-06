"""
join方法
"""
from multiprocessing import Process
import time


def test(name, i):
    print("%s is running" % name)
    time.sleep(i)
    print("%s is over" % name)


if __name__ == "__main__":
    p = Process(target=test, args=("lili", 1))
    p1 = Process(target=test, args=("keven", 2))
    p2 = Process(target=test, args=("json", 3))
    start_time = time.time()
    p.start()
    p1.start()
    p2.start()

    # p2.join()
    # p1.join()
    # 主进程代码等待子进程运行结束
    # p.join()
    print("主")
    last_time = time.time()
    print("time:", last_time - start_time)
