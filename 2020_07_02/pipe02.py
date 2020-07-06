"""
# 2.使用管道实现主进程和子进程之间的通信
"""
from multiprocessing import Process, Pipe


# 使用子进程来接受数据
def func(p):  # p 管道对象，其中管道的r端用来接收数据
    r, l = p  # 管道的左右两端，这个函数是用子进程来执行函数，只用到了r端，
    # 之所以写l端，是想说明进程中不用的管道要及时关闭
    l.close()  # 如果不关闭，程序就会阻塞
    while True:
        try:
            print(r.recv())  # 管道r端来接受数据
        except EOFError:
            break
    r.close()


if __name__ == "__main__":
    # 1.创建管道对象
    r, l = Pipe()
    p = Process(target=func, args=((r, l),))
    p.start()
    r.close()
    for i in range(10):
        l.send("hello jack %d" % i)
    l.close()

"""
 应该特别注意，管道端点的正确管理问题，
 如果是生产者或者消费者中都没有使用管道的某个端点，就应该将其关闭，
 这也说明为何在生产者（主进程中）关闭了管道的输出端（r端）在消费者中（子进程中）
 关闭了管道的输入端（l端），
 如果忘记执行这些步骤，程序有可能在消费者（子进程recv）recv()操作上挂起（阻塞），
 管道是由操作系统进行引用计数的，必须所有进程中关闭管道后，才能生产EOFError异常，所以在生产者（主进程）中关闭管道不会有任何效果，除非在消费者（子进程中）也关闭了相同的管道端点；
"""