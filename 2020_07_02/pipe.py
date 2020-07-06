"""
pipe.py
"""
# 1.进程间通信的第一个方法 pipe
# 原理：在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象，
# 进行读写操作，即可实现通信
from multiprocessing import Process, Pipe
import time

# 创建管道对象
fd1, fd2 = Pipe()

fd1.send("hello,lili")
print(fd2.recv())

fd2.send("hello,jack")
print(fd1.recv())
# fd2端只发送了一次数据，fd1端如果再次接受的话，就会阻塞
# 如果一端发送完数据之后直接把管道这端关闭，
# 另一端不断接收数据就会发生EOFError错误
# （我们可以捕获这种错误，当管道一端关闭时，另一端捕获到该类型的错误，直接也关闭就ok了）
fd2.close()
try:
    print(fd1.recv())
except Exception as e:
    print(e)
    fd1.close()





