#!/usr/bin/env python
"""
Module containing testing and timing methods
"""
import sys
import timeit
import numpy as np


OKAY = u'\033[92m'+u'\u2713'+u'\x1b[0m'
FAIL = u'\033[91m'+u'\u2717'+u'\x1b[0m'


def tnt(func, args=(), kwargs=(), repeats=3, loops=1000,
        test=None, output=True, verbose=True):
    """
    Test and time a function
    """
    if not isinstance(args, tuple):
        args = (args,)
    if not isinstance(kwargs, dict):
        kwargs = dict(kwargs)
    # preparing calls in strings
    __module__ = sys.argv[0].split('.')[0]
    arg_str = ", ".join(["{:d}"]*len(args)).format(*args)
    func_call = '{0:}.{1:}({2:})'.format(__module__, func.__name__, arg_str)
    import_call = 'import {}'.format(__module__)
    # actual testing
    time = timeit.repeat(func_call, setup=import_call,
                         repeat=repeats, number=loops)
    result = func(*args, **kwargs)
    if output:
        return_str = " -> {}".format(result)
        returns = (time, result)
    else:
        return_str = ""
        returns = time
    if test is not None:
        if isinstance(test, (list, np.ndarray)) and isinstance(result, (list, np.ndarray)):
            if all(test == result):
                return_str = " ".join([return_str, OKAY])
            else:
                return_str = " ".join([return_str, FAIL])
        else:
            if test == result:
                return_str = " ".join([return_str, OKAY])
            else:
                return_str = " ".join([return_str, FAIL])
    if verbose:
        print(func_call + return_str)
        print("{0:} loops, avg of {1:}:, {2:.4f} usec per loop".format(
            loops, repeats, sum(time)/repeats/loops*10**6))
    return returns
