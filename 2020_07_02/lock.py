from multiprocessing import Process, Lock
import time, json


# 互斥锁 当多个进程同时对一个数据进行操作时，会造成数据的混乱
# 查票
def search(i):
    with open('data', 'r', encoding='utf-8') as f:
        data = f.read()
    t_d = json.loads(data)
    # print(t_d)
    print('用户%s查询余票为:%s' % (i, t_d.get('ticket')))


# 买票
def buy(i):
    with open('data', 'r', encoding='utf-8') as f:
        data = f.read()
    t_d = json.loads(data)
    time.sleep(1)
    if t_d.get('ticket') > 0:
        # 票数减一
        t_d['ticket'] -= 1
        # 更新票数
        with open('data', 'w', encoding='utf-8') as f:
            json.dump(t_d, f)
        print('用户%s抢票成功' % i)
    else:
        print('没票了')


def run(i, mutex):
    search(i)
    mutex.acquire()  # 抢锁  只要有人抢到了锁 其他人必须等待该人释放锁
    buy(i)
    mutex.release()  # 释放锁


if __name__ == '__main__':
    mutex = Lock()  # 生成了一把锁
    for i in range(3):
        p = Process(target=run, args=(i, mutex))
        p.start()
