import time
from multiprocessing import Pool

COUNT = 500000000

def countdown(n):
    while n> 0:
        n -= 1
        

if __name__ == "__main__":
    n = 2
    pool = Pool(processes=n)
    time1 = time.time()
    for _  in range(n):
        pool.apply_async(countdown, [COUNT])
    
    pool.close()
    pool.join()
    time2 = time.time()
    print(f'Time taken in seconds :{time2 - time1}')
    
    