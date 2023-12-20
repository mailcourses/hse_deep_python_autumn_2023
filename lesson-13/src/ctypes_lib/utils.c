#include <stdio.h>
#include <stdlib.h>

//[10][1][5][3][9]
//  |
// arr |
//    arr+1

int sum(int* arr, int len)
{
    int res = 0;
    for (int i = 0; i < len; ++i)
    {
        res += arr[i];
    }
    return res;
}

int rfib(int n)
{
    if (n < 2)
        return 1;
    return rfib(n-1) + rfib(n-2);
}

int fib(int n)
{
    int a = 1, b = 1;
    for (int i = 0; i < n; ++i)
    {
        int tmp = a;
        a = a + b;
        b = tmp;
    }
    return b;
}
