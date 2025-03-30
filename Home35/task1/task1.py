import math
import time


def factorial(n):
    return math.factorial(n)


start_time = time.time()
factorial(10000)
factorial(20000)
factorial(30000)

end_time = time.time()
print(f"1 program time: {end_time - start_time} sec")


#  0.22-0.23 sec
