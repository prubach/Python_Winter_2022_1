#        * * * * * *
#         * * * * *
#          * * * *
#           * * *
#            * *
#             *
from time import time

n = 5

# How many bowls do I have given the n - number of rows


def sum_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        s = n + sum_bowls_recursive(n - 1)
        return s


def sum_bowls_loop(n):
    S = 0
    for i in range(1, n + 1):
        S = S + i
    return S


def sum_bowls_seq(n):
    return int(((1+n)/2)*n)


def time_func(func):
    t0 = time()
    func()
    t1 = time()
    elapsed = t1 - t0
    print('running {}, took: {}'.format(func, elapsed))

print('Sum using sequence: {} sum={}'.format(n, sum_bowls_seq(n)))
print('Sum using loop: {} sum={}'.format(n, sum_bowls_loop(n)))
print('Sum using recursion: {} sum={}'.format(n, sum_bowls_recursive(n)))