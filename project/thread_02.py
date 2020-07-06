"""
线程间通信
"""
from threading import Event, Thread
import threading
import time


def eat_huo_guo(name, event):
    print("%s 已经启动" % threading.current_thread().getName())
    print("%s 小伙伴已经进入就餐状态" % name)
    time.sleep(0.2)
    # event.wait()
    print("%s 小伙伴收到通知" % threading.current_thread().getName())
    print("%s 小伙伴开始吃饭了" % name)


if __name__ == "__main__":
    e = Event()
    # 设置线程组
    threads = []

    # 创建多个线程
    thread1 = Thread(target=eat_huo_guo, args=("a", e,))
    thread2 = Thread(target=eat_huo_guo, args=("b", e,))
    thread3 = Thread(target=eat_huo_guo, args=("c", e,))

    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

    for item in threads:
        item.start()

    # time.sleep(0.2)
    print("主线程通知小伙伴开饭了")
    # e.set()
