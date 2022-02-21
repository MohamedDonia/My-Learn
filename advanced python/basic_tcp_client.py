import logging
import socket

logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG,
                        #filename='log_file_name.log',
                        #filemode='w'
                        )

def download(server, port):
    '''
    Parameters
    ----------
    server : TYPE
        DESCRIPTION.
    port : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f"connecting to :{server}:{port}")
    
    s.connect(address)
    logging.info('connected')
    
    logging.info('send')
    s.send(b'Hello\r\n')
    
    logging.info('receive some data')
    data = s.recv(1024)
    
    logging.info('closing')
    s.close()
    
    logging.info(f'data: {data}')
    
    

def main():
    download("voidrealms.com", 80)
    


if __name__ == '__main__':
    main()