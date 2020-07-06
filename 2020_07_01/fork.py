"""
fork.py
"""

import os

pid = os.fork()

# windows上面没有fork调用
if pid < 0:
    print("create process failed")
elif pid == 0:
    print("new process")
else:
    print("old process")
