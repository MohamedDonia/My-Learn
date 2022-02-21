# Thread Locking
import time
from threading import Thread


def time_utils(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f'Time taken in seconds is {t2 - t1}')
    return wrapper


#@time_utils
def countdown(n):
    while n > 0:
        n -= 1
        

@time_utils
def countdown_multithread(t1, t2):
    t1.start()
    t2.start()
    t1.join()
    t2.join()


COUNT = 50000000

#countdown(COUNT)

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))
countdown_multithread(t1, t2)