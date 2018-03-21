#!/usr/bin/env python
"""
@author: phdenzel

Simple implementation of the Newton-Raphson method
"""


def derivative(f, x, h, *args, **kwargs):
    """
    Approximate a derivative for a function f
    """
    return (f(x+h, *args, **kwargs) - f(x-h, *args, **kwargs))/(2.*h)


def newton_raphson(f, x0, df=None, h=1e-6, epsilon=1e-15, verbose=False, **kwargs):
    """
    Use the Newton-Raphson method to find the root of a function f
    """
    if df is None:
        def df(x, *args, **kwargs):
            return derivative(f, x, h=h, **kwargs)
    xnext = x0 + 1
    xthis = x0
    iterations = 0
    while abs(xnext - xthis) > epsilon:
        xthis = xnext
        try:
            q = f(xnext, **kwargs)/df(xnext, **kwargs)
        except ZeroDivisionError:
            return xnext
        xnext = xnext - q
        iterations += 1
    if verbose:
        print("# of iterations:\t{}".format(iterations))
    return xnext


if __name__ == "__main__":
    def func1(x):
        """
        2^1/2
        """
        return x*x - 2

    def dfunc1(x):
        """
        The derivative of the first function
        """
        return 2*x

    xini = 2
    print(func1.__doc__)
    print("Derivative given".format(func1.__name__),
          newton_raphson(func1, xini, df=dfunc1, verbose=1))
    print("Derivative approx.".format(func1.__name__),
          newton_raphson(func1, xini, verbose=1))

    def func2(x):
        """
        (x-1)*(x-2)^2*(x+3) = 0
        """
        return (x-1)*(x-2)*(x-2)*(x+3)

    def dfunc2(x):
        """
        The derivative of the second function
        """
        return 4*x*x*x - 6*x*x - 14*x + 20

    xini = 3
    print(func2.__doc__)
    print("Derivative given".format(func2.__name__),
          newton_raphson(func2, xini, df=dfunc2, verbose=1))
    print("Derivative approx.".format(func2.__name__),
          newton_raphson(func2, xini, verbose=1))

    def func3(x):
        """
        1729.03^(1/3)
        """
        return x*x*x - 1729.03

    def dfunc3(x):
        """
        The derivative of the third function
        """
        return 3*x*x

    xini = 12
    print(func3.__doc__)
    print("Derivative given".format(func3.__name__),
          newton_raphson(func3, xini, df=dfunc3, verbose=1))
    print("Derivative approx.".format(func3.__name__),
          newton_raphson(func3, xini, verbose=1))

    def func4(x):
        """
        x^3 + x = 42
        """
        return x*x*x + x - 42

    def dfunc4(x):
        """
        The derivative of the forth function
        """
        return 3*x*x + 1

    xini = 3
    print(func4.__doc__)
    print("Derivative given".format(func4.__name__),
          newton_raphson(func4, xini, df=dfunc4, verbose=1))
    print("Derivative approx.".format(func4.__name__),
          newton_raphson(func4, xini, verbose=1))
