# https://medium.com/@ark.iitkgp/concurrency-in-python-understanding-threading-multiprocessing-and-asyncio-03bd92ca298b

import multiprocessing
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)  # Simulate some work
    print(f"Worker {name} finished")
if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()  # Wait for all processes to finish

    print("Main process finished. All workers finished.")