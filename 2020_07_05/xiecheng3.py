"""
greelet.py
"""
from greenlet import greenlet


def test1():
    print("执行text1")
    gr2.switch()
    print("结束text1")
    gr2.switch()


def test2():
    print("执行text2")
    gr1.switch()
    print("结束text2")


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()  # 选择执行协程1
