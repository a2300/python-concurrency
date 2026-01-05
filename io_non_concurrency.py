# From https://realpython.com/python-concurrency/
import time

import requests

def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(session, url)

def download_site(session, url):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

if __name__ == "__main__":
    main()

# Output:
# (.venv) Yuriy_Buy ~/IdeaProjects/python-concurrency  $ python ./io_non_concurrency.py
# ...
# Downloaded 160 sites in 13.64336529100001 seconds