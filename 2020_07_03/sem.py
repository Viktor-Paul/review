"""

"""
from multiprocessing import Process, Semaphore
import time


def hello(sema):
    sema.acquire()
    print(sema.get_value())
    print('调用进程')
    sema.release()



if __name__ == "__main__":
    # 信号量管理表示realse()调用数减去acquire()调用数加上去一个初始值的计数器　　1　-　5　+　0　＝　-4　
    sema = Semaphore(3)

    t = Process(target=hello, args=(sema,))
    t1 = Process(target=hello, args=(sema,))
    t2 = Process(target=hello, args=(sema,))
    t.start()
    t1.start()
    t2.start()
    t.join()
    t1.join()
    t2.join()

    time.sleep(3)
    print('开启进程')

