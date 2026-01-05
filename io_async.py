# From https://realpython.com/python-concurrency/
import asyncio
import time

import aiohttp


async def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    await download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(session, url) for url in sites]
        await asyncio.gather(*tasks)

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {len(await response.read())} from {url}")


if __name__ == "__main__":
    asyncio.run(main())

# Output:
# (.venv) Yuriy_Buy ~/IdeaProjects/python-concurrency  $ python ./io_async.py
# ...
# Downloaded 160 sites in 0.6183204579992889 seconds