import asyncio
import unittest
from unittest import mock
import time
from functools import partial
from fetcher import fetch_url, fetch_batch

URL = "https://docs.python.org/3/whatsnew/3.12.html"


class TestFetcher(unittest.IsolatedAsyncioTestCase):

    async def test_fetch_url(self):
        with mock.patch("fetcher.aiohttp.ClientSession.get") as amock:
            text_mock = mock.AsyncMock(return_value="orig_resp")
            resp_mock = mock.AsyncMock(text=text_mock)
            amock.return_value.__aenter__.return_value = resp_mock

            res = await fetch_url("test_url")

            self.assertEqual("orig_resp", res)

            expected_calls = [
                mock.call("test_url"),
                mock.call().__aenter__(),
                mock.call().__aenter__().text(),
                mock.call().__aexit__(None, None, None),
            ]
            self.assertEqual(expected_calls, amock.mock_calls)

    async def test_fetch_url_error(self):
        with mock.patch("fetcher.aiohttp.ClientSession.get") as amock:
            amock.side_effect = Exception("http error")

            with self.assertRaises(Exception):
                res = await fetch_url("test_url")

            expected_calls = [
                mock.call("test_url"),
            ]
            self.assertEqual(expected_calls, amock.mock_calls)

    async def test_fetch_batch_url(self):
        urls = [f"url_{i}" for i in range(1, 5)]
        workers = 1

        with mock.patch("fetcher.aiohttp.ClientSession.get") as amock:
            text_mock = mock.AsyncMock(side_effect=[f"resp_{u}" for u in urls])
            resp_mock = mock.AsyncMock(text=text_mock)
            amock.return_value.__aenter__.return_value = resp_mock

            await fetch_batch(urls, workers)

            amock.assert_has_calls(
                [mock.call(url) for url in urls],
                any_order=True,
            )
            self.assertEqual(len(urls), amock.call_count)

    async def commit_fetch_batch_url_time(self, workers, urls):
        with mock.patch("fetcher.aiohttp.ClientSession.get") as amock:
            text_mock = mock.AsyncMock(
                side_effect=partial(asyncio.sleep, 0.1)
            )
            resp_mock = mock.AsyncMock(text=text_mock)
            amock.return_value.__aenter__.return_value = resp_mock

            start = time.time()
            await fetch_batch(urls, workers)
            end = time.time()

            amock.assert_has_calls(
                [mock.call(url) for url in urls],
                any_order=True,
            )
            self.assertEqual(len(urls), amock.call_count)

        return end - start

    async def test_commit_time(self):
        urls = [f"url_{i}" for i in range(1, 50)]

        for workers in (1, 10, 30):
            total_time = await self.commit_fetch_batch_url_time(workers, urls)
            print(f"{workers=}, {total_time=}")



if __name__ == "__main__":
    unittest.main()
