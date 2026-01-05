import asyncio

async def greering_after_delay():
    print("Starting...")
    await asyncio.sleep(2)
    print(f"Hello")

asyncio.run(greering_after_delay())
