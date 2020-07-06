import random
import time

first_time = time.time()
list01 = []
for i in range(1000000):
    a = random.randint(1, 1000000)
    list01.append(a)

last_time = time.time()
print(last_time - first_time)

