import time

"""
Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""


def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        res_time = end_time - start_time
        print(f"Performance time: {res_time}")
    return wrapper


@decorator
def function():
    print("First hello!")
    time.sleep(1.3)
    print("Second hello!")


print(function())
