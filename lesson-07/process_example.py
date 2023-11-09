import multiprocessing as mp
import time
import os


def launch_child(n):
    print(f"{os.getpid()=}, {os.getppid()=}")
    time.sleep(n)


if __name__ == "__main__":
    pr = mp.Process(target=launch_child, args=(10,), name="launch_child_process")
    print(pr.name)
    pr.start()
    pr.join()

    print("end")
