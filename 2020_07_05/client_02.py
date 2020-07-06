"""
client.py
"""
from socket import *

socked = socket()

socked.connect(("127.0.0.1", 8888))

while True:
    data = input("msg>>")
    if not data:
        break
    socked.send(data.encode())
    result = socked.recv(1024)
    print("server data", result.decode())
socked.close()
