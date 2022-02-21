import logging
from threading import Thread
import time
import random

# define function 
def longtask(name):
    Max = random.randrange(1,10)
    logging.info(f'Task: {name} performing {str(Max)}')
    for x in range(Max):
        logging.info(f'task {name}: {x}')
        time.sleep(random.randrange(1,3))
    logging.info(f'Task: {name}: complete')
        



def main():
    logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )
    logging.info('Started')
    #longtask('main')
    threads = []
    for x in range(10):
        t = Thread(target=longtask, args=['thread' + str(x)])
        threads.append(t)
        t.start()
        
    # wait for all threads to fininsh 
    for t in threads:
        t.join()
        
    logging.info('Finished all threads')
    

if __name__ == '__main__':
    main()
    

