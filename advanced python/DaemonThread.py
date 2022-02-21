import time 
import threading
from threading import Timer, Thread
import logging
import random 

def test():
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    for x in range(6):
        logging.info(f'Working: {threadname}')
        time.sleep(1)
    logging.info(f'Finished: {threadname}')



def stop():
    logging.info('Exiting the applicaton')
    exit(0)
    
    
    
    
    
def main():
    logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s %(threadName)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )
    logging.info('Main thread started')
    timer =Timer(3, stop)
    timer.start()
    
    # thread 
    t = Thread(target=test,daemon=True)
    t.start()
    logging.info('Main thread finished')
    
    

if __name__ == "__main__":
    main()