"""
使用管道实现生产者和消费者模式
"""
# 由于管道默认没加锁，数据不安全，所以在消费者模型中，
# 需要对子进程加锁，同一时间只有一个子进程执行消费者模型，操作里面的数据：

from multiprocessing import Process, Pipe, Lock


# 消费者模型
def fun1(p, lock):  # lock是给子进程加锁，防止多个进程同时操作数据，保证数据安全（管道默认没加锁，数据不安全）
    r, l = p
    l.close()
    while True:
        try:
            lock.acquire()
            print(r.recv())
            lock.release()
        except EOFError:
            lock.release()
            break
    r.close()


# 生产者模型
def fun2(p):
    r, l = p
    r.close()
    for i in range(10):
        l.send("hello jack %d" % i)
    l.close()


if __name__ == "__main__":
    # 创建对象
    r, l = Pipe()
    lock = Lock()
    p1 = Process(target=fun1, args=((r, l), lock))
    p2 = Process(target=fun1, args=((r, l), lock))
    p1.start()
    p2.start()
    p3 = Process(target=fun2, args=((r, l),))
    p4 = Process(target=fun2, args=((r, l),))
    p5 = Process(target=fun2, args=((r, l),))
    p3.start()
    p4.start()
    p5.start()
    r.close()
    l.close()
