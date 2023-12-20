
cpdef rfib(int n):
    if n < 2:
        return 1
    return rfib(n-1) + rfib(n-2)

cpdef fib(int n):
    cdef int a = 1
    cdef int b = 1
    cdef int i
    for i in range(n):
        a, b = a+b, a
    return b
