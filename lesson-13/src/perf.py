#! /usr/bin/env python3

import time
import ctypes

import pyximport
import cffi

import cutils

N = 36

def rfib(n):
    if n < 2:
        return 1
    return rfib(n-1) + rfib(n-2)

def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a,b = a+b, a
    return b

def pour_python():
    start_ts = time.time()
    rres = rfib(N)
    end_ts = time.time()
    print(f"[python] rres = {rres}, time = {end_ts - start_ts}")
    start_ts = time.time()
    res = fib(N)
    end_ts = time.time()
    print(f"[python] res = {res}, time = {end_ts - start_ts:.09f}")

def cython():
    import cyutils
    start_ts = time.time()
    rres = cyutils.rfib(N)
    end_ts = time.time()
    print(f"[cython] rres = {rres}, time = {end_ts - start_ts}")
    start_ts = time.time()
    res = cyutils.fib(N)
    end_ts = time.time()
    print(f"[cython] res = {res}, time = {end_ts - start_ts:.09f}")

def ctypes_fib():
    lib = ctypes.cdll.LoadLibrary('./ctypes_lib/libutils.so')
    lib.fib.restype = ctypes.c_int
    lib.fib.argstype = [ctypes.c_int]
    lib.rfib.restype = ctypes.c_int
    lib.rfib.argstype = [ctypes.c_int]

    start_ts = time.time()
    rres = lib.rfib(N)
    end_ts = time.time()
    print(f"[ctypes] rres = {rres}, time = {end_ts - start_ts}")
    start_ts = time.time()
    res = lib.fib(N)
    end_ts = time.time()
    print(f"[ctypes] res = {res}, time = {end_ts - start_ts:.09f}")

def cffi_fib():
    ffi = cffi.FFI()
    cffi_lib = ffi.dlopen('./cffi_lib/libutils.so')
    ffi.cdef('''
    int rfib(int);
    int fib(int);
    ''')

    start_ts = time.time()
    rres = cffi_lib.rfib(N)
    end_ts = time.time()
    print(f"[cffi] rres = {rres}, time = {end_ts - start_ts}")
    start_ts = time.time()
    res = cffi_lib.fib(N)
    end_ts = time.time()
    print(f"[cffi] res = {res}, time = {end_ts - start_ts:.09f}")

def capi():
    start_ts = time.time()
    rres = cutils.rfib(N)
    end_ts = time.time()
    print(f"[capi] rres = {rres}, time = {end_ts - start_ts}")
    start_ts = time.time()
    res = cutils.fib(N)
    end_ts = time.time()
    print(f"[capi] res = {res}, time = {end_ts - start_ts:.09f}")

def main():
    pour_python()
    cython()
    ctypes_fib()
    cffi_fib()
    capi()

if __name__ == "__main__":
    pyximport.install()
    main()
