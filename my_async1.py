import time

def greet_after_delay():
    print("Starting...")
    time.sleep(2)  # Blocks for 2 seconds
    print("Hello!")

greet_after_delay()