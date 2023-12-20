#include <stdlib.h>
#include <stdio.h>

struct Point
{
    int x;
    int y;
    char val;
};

int area(struct Point* p1, struct Point* p2)
{
    printf("p1->val = %c, p2->val = %c\n", p1->val, p2->val);
    return abs((p2->y - p1->y) * (p2->x - p1->x));
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
