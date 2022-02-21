import time 
import threading
from concurrent.futures import ThreadPoolExecutor
import logging
import random 

counter = 0 


def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting : {threadname}')
    
    for x in range(count):
        logging.info(f'Count: {threadname} += {count}')
        # the blobal interpreter lock GIL
        '''
        lock = threading.Lock()
        lock.acquire()
        #lock.acquire()   # dead lock
        try:
            count += 1
        finally:
            lock.release()
        '''
        # simplified lock
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {threadname}')
            counter +=1
            time.sleep(2)
            

    logging.info(f'Completed : {threadname}')
 

def main():
    logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s %(threadName)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )
    logging.info('AppStarted')
    
    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test, v)
    logging.info('AppFinished')   
    
    
    
if __name__ == "__main__":
    main()    