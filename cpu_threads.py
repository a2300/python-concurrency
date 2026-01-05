import time
from concurrent.futures import ThreadPoolExecutor

def main():
    start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fib, [35] * 20)
    duration = time.perf_counter() - start_time
    print(f"Computed in {duration} seconds")

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

if __name__ == "__main__":
    main()

# Output:
# (.venv) Yuriy_Buy ~/IdeaProjects/python-concurrency  $ python ./cpu_threads.py
# Computed in 15.754992042000595 seconds