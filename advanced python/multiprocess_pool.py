import logging
import multiprocessing
from multiprocessing.context import Process
import time
import random


def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started: {item}')
    for x in range(count):
        logging.info(f'name: {item} = {x}')
        time.sleep(1)
        
    logging.info(f'{name} Finished: {item}')
    return item + 'is finished'




def proc_results(result):
    logging.info(f'Results: {result}')


def main():
    logging.info('Started !')
    max_ = 5
    pool = multiprocessing.Pool(max_)
    results = []
    for x in range(max_):
        item = "Item" + str(x)
        count = random.randrange(1, 5)
        r = pool.apply_async(work, [item, count], callback=proc_results)
        results.append(r)
        
    # wait for process
    for r in results:
        r.wait()
        
    # pool.close or pool.terminate
    pool.close()
    pool.join()
    logging.info('Finished !')
    
        
        
        
        
logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
if __name__ == '__main__':
    main()
    
    