import logging
import threading 
from concurrent.futures import ThreadPoolExecutor
import time
import random 




def test(item):
    s = random.randrange(1, 10)
    logging.info(f'Thread {item}: id = {threading.get_ident()} sleeping for {s}')
    #logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    #logging.info(f'Thread {item}: sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')





def main():
    logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )
    logging.info('AppStarted')
    
    workers = 5
    items = 15
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test, range(items))
    
    logging.info('AppFinished')



if __name__ == "__main__":
    main()