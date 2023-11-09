import multiprocessing as mp


class MultyA:
    def __init__(self, val):
        self.val = val


def update_data(data):
    print("update_data", data, id(data))
    data["updated"] = [1, 2 ,10]
    data["qwerty"] = MultyA(42)


if __name__ == "__main__":
    data = {}
    print(data, id(data))

    pr = mp.Process(target=update_data, args=(data,))
    pr.start()
    pr.join()

    print(data, id(data))

    print("-------")

    with mp.Manager() as manager:
        data = manager.dict()
        print(data, id(data))

        pr = mp.Process(target=update_data, args=(data,))
        pr.start()
        pr.join()

        print(data, id(data))
        print(data["qwerty"].val)

