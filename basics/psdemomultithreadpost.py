"""multi threaded http client"""

import threading
from time import perf_counter
import requests



def make_post(data):
    """child thread"""
    url = 'https://reqres.in/api/users'
    res = requests.post(url, json=data)
    print(res.status_code, res.json())


def main():
    """main thread"""
    payload = [('tim', 'manager'), ('nat', 'director'), ('pat', 'clerk'), ('nick', 'helper')]
    names = ['name', 'job']

    list_of_threads = []
    start = perf_counter()

    for person in payload:
        data_set = dict(zip(names, person))
        t = threading.Thread(target=make_post, args=(data_set,))
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()   # block the execution of the main thread till the joined thread terminates

    print(perf_counter() - start)


if __name__ == '__main__':
    main()
# concurrency
# multi threading
# multi processing
