# -*- coding: utf-8 -*-
"""
@author: phdenzel

Program to compute Bernoulli numbers (first computer program ever written)

Ada's note G:
How to compute functions with the 'Analytical Engine'...

Ada's Formula:
B_n = 1/2*(2*n-1)/(2*n+1) - sum from m to n-1 ( [(2n)!] / [(2m)!*(2n-2m+1)!] ) * B_m

These indices aren't the commonly used ones...
... and other non-recursive algorithms would probably be faster
... which is why I use memoization
"""
from fractions import Fraction


def memoize(func):
    memo = {}
    def wrapper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return wrapper

@memoize
def factorial(n):
    """
    Recursive algorithm for factorials
    """
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)

@memoize
def bernoulli(n):
    """
    Calculate the n-th Bernoulli number following to Ada's program
    """
    if n == 1:
        return Fraction(1, 6)
    else:
        b = 0
        for m in range(1, n):
            b_frac = Fraction(factorial(2*n), factorial(2*m)*factorial(2*n-2*m+1))
            b += b_frac * bernoulli(m)
        return Fraction(1, 2)*Fraction(2*n-1, 2*n+1) - b


if __name__ == '__main__':
    for n in range(100):
        s = bernoulli(n)
        print(s)
