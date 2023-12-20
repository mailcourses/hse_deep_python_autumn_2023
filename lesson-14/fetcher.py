import asyncio
import aiohttp
import time

URL = "https://docs.python.org/3/whatsnew/3.12.html"
URLS = [URL] * 20
WORKERS_NUM = 10


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text()
            # print(f"resp for {url=} is {data=}")
            return data


async def fetch_worker(que, i):
    while True:
        url = await que.get()
        try:
            result = await fetch_url(url)
        finally:
            que.task_done()


async def fetch_batch(urls, workers_num):
    workers = []
    que = asyncio.Queue()

    for i in range(workers_num):
        workers.append(asyncio.create_task(fetch_worker(que, i)))

    for url in urls:
        await que.put(url)

    await que.join()

    for worker in workers:
        worker.cancel()


if __name__ == "__main__":
    t1 = time.time()

    asyncio.run(fetch_batch(URLS, WORKERS_NUM))

    t2 = time.time()
    print(t2 - t1)
