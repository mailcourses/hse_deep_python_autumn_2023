import multiprocessing as mp
import time
import os

N = 10 ** 8
N_PROC = 4
COUNT_SIZE = N // N_PROC


def counter(a, b):
    print(f"PROC: {os.getpid()=}")
    while a < b:
        a += 1


if __name__ == "__main__":
    t1 = time.time()
    counter(0, N)
    t2 = time.time()
    print(t2 - t1)

    t1 = time.time()
    procs = [
        mp.Process(
            target=counter,
            args=(i * COUNT_SIZE, (i + 1)* COUNT_SIZE),
            name=f"counter_proc_{i}",
        )
        for i in range(N_PROC)
    ]

    t1_start = time.time()
    for pr in procs:
        pr.start()
    t2_start = time.time()
    print("start", t2_start - t1_start)

    for pr in procs:
        pr.join()

    t2 = time.time()
    print(t2 - t1)
