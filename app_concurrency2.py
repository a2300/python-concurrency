# https://medium.com/@ark.iitkgp/concurrency-in-python-understanding-threading-multiprocessing-and-asyncio-03bd92ca298b

import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)  # Simulating I/O-bound work
    print(f"Worker {name} finished")
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()  # Wait for all threads to complete

print("Main thread finished. All workers finished.")