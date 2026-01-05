import asyncio

async def slow_operation():
    print("Starting slow operation...")
    await asyncio.sleep(5)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=3)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("The operation timed out!") 

asyncio.run(main())