#! /usr/bin/env python

import random
import ctypes

def main():
    lib = ctypes.cdll.LoadLibrary('./libutils.so')
    lib.sum.restype = ctypes.c_int
    lib.sum.argstype = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    l = list(range(20))
    random.shuffle(l)
    l = l[:15]
    print(l)
    arr_type = ctypes.c_int * len(l)
    res = lib.sum(arr_type(*l), len(l))
    expected = sum(l)
    print(f'csum = {res}, expected = {expected}')
    assert(expected == res)

if __name__ == "__main__":
    main()
