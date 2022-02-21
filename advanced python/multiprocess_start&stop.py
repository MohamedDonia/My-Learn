import logging 
import multiprocessing
from multiprocessing.context import Process 
import time

def work(msg, max_):
    name = multiprocessing.current_process().name
    logging.info(f'{name} Started')
    
    for x in range(max_):
        logging.info(f'{name} {msg}')
        time.sleep(1)
        
    logging.info(f'{name} Finished')
        

def main():
    logging.info("Started")
    max_ = 3
    worker = Process(target=work, args=['work', max_], daemon=True, name='Worker')
    worker.start()
    
    
    time.sleep(5)
    if worker.is_alive():
        worker.terminate()
    
    worker.join()
    
    logging.info(f'Finished: {worker.exitcode}')
    


    
    
    
logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d %(message)s",
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


if __name__ == "__main__":
    main()    
        
    