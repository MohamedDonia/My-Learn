# async code 
# async runs in the same thread
# async uses coroutines which run on the same thread
# we also introduce the "async" and "await" keywords

# Thread is a slice of time on 

import threading
import multiprocessing
import logging
import asyncio
import random

logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d %(message)s",
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}: {msg}')
    

async def work(name):
    display(name + ' starting')
    await asyncio.sleep(random.randint(1, 10))
    display(name + ' finished')

async def run_async(max_):
    tasks = []
    for x in range(max_):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name)))
        
    await asyncio.gather(*tasks)



def main():
    display("Main Started")
    
    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(run_async(10))
    loop.close()
    
    display("main Finished")        
    



if __name__ == '__main__':
    main()