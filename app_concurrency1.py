# https://medium.com/@ark.iitkgp/concurrency-in-python-understanding-threading-multiprocessing-and-asyncio-03bd92ca298b

import threading
import time

def print_numbers():
    # This function will run in a separate thread
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# Create a thread that runs the print_numbers function
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Main thread finished.")