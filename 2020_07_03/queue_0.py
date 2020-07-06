"""
消息队列实现进程间的通信
"""
# 1.原理：在内存中建立队列模型，进程通过把消息存入队列，从队列取出消息，完成进程间的通信
from multiprocessing import Queue

# 1.创建对象
q = Queue(3)

q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

if not q.full():
    q.put("消息4")

if not q.empty():
    for i in range(q.qsize()):
        print(q.get(False))

