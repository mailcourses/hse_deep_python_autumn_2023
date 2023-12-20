import multiprocessing as mp
import socket
import time


def client(data):
    print("client")

    time.sleep(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("localhost", 21000))

        sock.sendall(data.encode())
        print("client recv back", sock.recv(4096))


def server():
    print("server")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("localhost", 21000))
        sock.listen(5)

        client_sock, addr = sock.accept()
        print(f"server conn from: {addr=}")
        with client_sock:
            client_sock.setblocking(0)
            data = b""
            while True:
                try:
                    part = client_sock.recv(5)
                except Exception as err:
                    print("ERROR", err)
                    break
                else:
                    print("recv part", part)
                    data += part

            print("===== total data:", data)
            client_sock.sendall(data.upper())


if __name__ == "__main__":
    srv_pr = mp.Process(target=server)
    cl_pr = mp.Process(target=client, args=("qwerty1234567890",))

    srv_pr.start()
    cl_pr.start()

    srv_pr.join()
    cl_pr.join()

