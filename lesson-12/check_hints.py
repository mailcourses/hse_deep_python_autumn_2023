from typing import Any, Callable, Generator, Iterable, Sequence, TypeVar
import argparse


T = TypeVar("T")
TRes = TypeVar("TRes")


def add_nums(a: int, b: int) -> list:
    return [a + b]


def concat(a: str, b: str) -> str:
    return a + b


def apply_function(
    fn: Callable[[T, T], TRes],
    a: T,
    b: T,
) -> TRes:
    return fn(a, b)


def run_check_genenric() -> None:
    print(apply_function(add_nums, 10, 20))
    print(apply_function(concat, "a", "b"))


class Edx:
    pass


FetchResp = dict[str, str | int | list]
FetchRespNew = dict[str, str | int | list | dict | Edx]


def fetch_url(url: str) -> FetchResp:
    return {"name": "Steve", "age": 99, "games": []}


def fetch_url_new(url: str) -> FetchRespNew:
    return {"name": "Steve", "age": 99, "games": [], "bank": {}, "edx": Edx()}


def run_check_fetch() -> None:
    url = "some_url"

    data: FetchResp | FetchRespNew
    if len(url) > 3:
        data = fetch_url(url)
    else:
        data = fetch_url_new(url)

    print(data)


def get_max_temp(temps: Iterable[int]) -> int | None:
    if not temps:
        return None

    return max(temps)


def get_first_temp(temps: Sequence[int]) -> int | None:
    if not temps:
        return None

    return temps[0]


def run_check_temp() -> None:
    print()
    temps = [1, 2 ,5, -10, 32, 20]
    temp = get_max_temp(temps)
    print(f"max {temp=} from {temps=}")

    temps1 = (1, 2 ,5, -10, 32, 20)
    temp = get_max_temp(temps1)
    print(f"max {temp=} from {temps=}")

    temps = []
    temp = get_max_temp(temps)
    print(f"max {temp=} from {temps=}")

    temps = [1, 2 ,5, -10, 32, 20]
    temp = get_first_temp(temps)
    print(f"first {temp=} from {temps=}")

    temps1 = (1, 2 ,5, -10, 32, 20)
    temp = get_first_temp(temps1)
    print(f"first {temp=} from {temps=}")

    temps = []
    temp = get_first_temp(temps)
    print(f"first {temp=} from {temps=}")

    gen = (i for i in range(5))
    temp = get_max_temp(gen)
    print(f"max {temp=} from {gen=}")

    # gen = (i for i in range(5))
    # temp = get_first_temp(gen)
    # print(f"first {temp=} from {gen=}")

    def gen_z() -> Generator[int, int, str]:
        s: int = yield 10
        s = yield 30
        s = yield 30

        return "finished"

    g = gen_z()
    next(g)
    g.send(42)


if __name__ == "__main__":
    run_check_fetch()
    run_check_temp()
    run_check_genenric()

    args = argparse.argparse()
