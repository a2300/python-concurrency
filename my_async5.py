import asyncio

async def fetch_number(number):
    await asyncio.sleep(1)  # Simulate an I/O-bound operation
    return number * 10

async def main():
    results = await asyncio.gather(
        fetch_number(1),
        fetch_number(2),
        fetch_number(3)
    )
    print("Fetched numbers:", results)

asyncio.run(main())