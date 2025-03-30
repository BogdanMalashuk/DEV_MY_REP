import math
import time
import threading


def factorial(n):
    return math.factorial(n)


start_time = time.time()

threads = []
for i in range(3):
    thread = threading.Thread(target=factorial, args=((i + 1) * 10000,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"2 program time: {end_time - start_time} sec")


#  0.22-0.23 sec
