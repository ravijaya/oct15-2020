import threading
from time import sleep
from random import random


def worker(delay):
    """child thread function"""
    t_name = threading.currentThread().name
    t_id = threading.currentThread().ident
    sleep(delay)
    print(f'{t_name} with #id: {t_id} waited for the {delay}')  # critical section of the code


def main():
    """main thread function"""
    list_of_threads = []

    for item in range(1, 6):
        delay_time = random()
        t = threading.Thread(target=worker, args=[delay_time], name=f't{item}')
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()   # block the execution of the main thread till the joined thread terminates

    print(threading.currentThread().name, 'prepares to terminate !!!!')


if __name__ == '__main__':
    main()
