import asyncio
import time

async def greet_after_delay(name):
    print(f"Starting {name}...")
    await asyncio.sleep(2)
    print(f"Hello, {name}!")

async def main():
    start = time.perf_counter()
    
    await greet_after_delay("Alice")
    await greet_after_delay("Bob")
    await greet_after_delay("Charlie")
    
    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f} seconds")

asyncio.run(main())