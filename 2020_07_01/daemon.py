from multiprocessing import Process
import time


def test(name):
    print('%s总管正常活着' % name)
    time.sleep(3)
    print('%s总管正常死亡' % name)


if __name__ == '__main__':
    p = Process(target=test, args=('egon',))
    # p.daemon = True  # 将该进程设为守护进程   这句话必须放在start语句之前 否则报错
    p.start()
    time.sleep(0.1)
    print('皇帝jason寿正终寝')
