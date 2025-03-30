import math
import time
import multiprocessing


def factorial(n):
    return math.factorial(n)


if __name__ == "__main__":
    start_time = time.time()

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(factorial, [(i + 1) * 10000 for i in range(3)])

    end_time = time.time()
    print(f"3 program time: {end_time - start_time} sec")


#  0.10-0.11 sec
