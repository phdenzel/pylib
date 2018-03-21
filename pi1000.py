#!/usr/bin/env python
"""
@author: phdenzel

Program to compute the first 1000 digits of pi with Machin's formula
"""
from fractions import Fraction


def arctan(p, q, precision=Fraction(1, 10**1000)):
    """
    Calculate arctan with a Taylor series upto a certain precision

    Taylor expansion: arctan(x) ~ x − x**3/3 + x**5/5 − x**7/7 + ...
    """
    xterm = Fraction(p, q)
    denom = 1
    series = xterm
    term = xterm/denom
    x2 = -xterm*xterm
    while abs(term) > precision:
        xterm *= x2
        denom += 2
        term = xterm/denom
        series += term
    return series


if __name__ == '__main__':
    prec = 10**1000
    pi = 16*arctan(1, 5, precision=Fraction(1, prec)) - 4*arctan(1, 239, precision=Fraction(1, prec))
    pidigits = str(int(pi*prec))
    print("{0:}.{1:}".format(pidigits[0], pidigits[1:]))

