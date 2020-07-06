import multiprocessing as mp
from time import sleep

a = 1


def fun():
    print("开始一个新的进程")
    sleep(5)
    global a
    print("a = ", a)
    a = 10000
    print("a = ", a)
    print("子进程结束了")


# 创建进程对象
if __name__ == "__main__":
    p = mp.Process(target=fun)
    p.start()  # 启动进程
    sleep(2)
    print("父进程干点啥")

    p.join(1)  # 回收进程

    print('a:', a)
    sleep(7)
    print('a:', a)
