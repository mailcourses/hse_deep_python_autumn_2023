import multiprocessing
import time


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    N = 5 * 10 ** 7
    N_PROCS = 4

    t1 = time.time()
    for _ in range(N_PROCS):
        countdown(N)
    t2 = time.time()
    print(t2 - t1)

    t1 = time.time()
    with multiprocessing.Pool(N_PROCS) as p:
        print("start", time.time())
        p.apply(countdown, (N,))
        print("finish", time.time())

        p.map(countdown, [N] * N_PROCS)

        for _ in range(N_PROCS):
            p.apply_async(countdown, (N,))
        p.close()
        p.join()
    t2 = time.time()

    print(t2 - t1)
