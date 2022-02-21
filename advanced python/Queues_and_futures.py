import time 
import threading
from threading import Thread
from queue import Queue
import logging
import random 
from concurrent.futures import ThreadPoolExecutor


#Queues 


def test(name, que):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finished: {threadname}')
    ret  = 'Hello ' + name + ' your random number is: ' + str(random.randrange(1,10))
    que.put(ret)
    

def queued():
    que = Queue()
    t = Thread(target = test, args = ['mohamed', que,])
    t.start()
    logging.info('Do something on the main thread')
    t.join()
    
    ret = que.get()
    logging.info(f'Returned: {ret}')


# main
def main():
    logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s %(threadName)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )
    logging.info('Main thread started')
    queued()
    
    

if __name__ == "__main__":
    main()