"""
server.py
"""
import mmap
import contextlib
import time

with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_WRITE)) as m:
    for i in range(1, 10001):
        m.seek(0)
        m.write(("msg " + str(i)).encode())
        m.flush()
        time.sleep(1)
