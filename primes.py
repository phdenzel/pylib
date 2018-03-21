# -*- coding: utf-8 -*-
"""
@author: phdenzel

Methods for generating primes
"""
from time_and_test import tnt
import numpy as np
from matplotlib import pyplot as plt


def eratosthenes(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    """
    if isinstance(limit, (int, float)) and limit == int(limit):
        limit = int(limit)
    else:
        raise ValueError
    primes = []
    mask = [1]*(limit+1)
    for i in range(2, limit+1):
        if mask[i]:
            primes.append(i)
            for j in range(i*i, limit+1, i):
                mask[j] = 0
    return np.asarray(primes)


def eratosthenes_mem(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    while conserving memory

    TODO: check again... still buggy
    """
    if isinstance(limit, (int, float)) and limit == int(limit):
        limit = int(limit)
    else:
        raise ValueError
    primes = [2]
    multiples = [2]
    limit += 1
    for candidate in range(3, limit):
        if candidate not in multiples:
            primes.append(candidate)
            multiples.append(2*candidate)
        for i, m in enumerate(multiples):
            if m <= candidate:
                multiples[i] += primes[i]
    return np.asarray(primes)


def eratosthenes_np(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    utilizing numpy arrays and methods
    """
    if isinstance(limit, (int, float)):
        limit = int(limit)
    else:
        raise ValueError
    mask = np.ones(limit+1, dtype=np.bool)
    mask[:2] = False
    for i in range(2, int(np.sqrt(limit))+1):
        if mask[i]:
            mask[i*i::i] = False
    return np.nonzero(mask)[0]


def eratosthenes_npo(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    utilizing numpy arrays and methods, trying to conserve memory
    """
    if isinstance(limit, (int, float)):
        limit = int(limit)
    else:
        raise ValueError
    mask = np.ones(limit//2, dtype=np.bool)
    for i in range(3, int(limit**0.5)+1, 2):
        if mask[i//2]:
            mask[i*i//2::i] = False
    return np.r_[2, 2*np.nonzero(mask)[0][1::]+1]


def prime_dist(func, n):
    """
    Plots primes up to n using func(n)
    [p_k] versus [k * log(p_k)]; with k: order of prime
    """
    x = func(n)
    y = list(range(len(x)))
    for i in range(len(x)):
        y[i] = (i+1)*np.log(x[i])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel(r'k $\cdot$ log(p$_k$)')
    ax.set_xlabel(r'p$_k$')
    plt.suptitle('Distribution of primes', fontsize=15)
    ax.plot(x, y, lw=2, color='#FE4365')
    plt.show()


if __name__ == "__main__":
    n = 1000000
    primes = eratosthenes(n)

    tnt(eratosthenes, args=(n), repeats=3, loops=10, test=primes)
    # tnt(eratosthenes_mem, args=(n), repeats=3, loops=10, test=primes)
    tnt(eratosthenes_np, args=(n), repeats=3, loops=10, test=primes)
    tnt(eratosthenes_npo, args=(n), repeats=3, loops=10, test=primes)

    prime_dist(eratosthenes_npo, n)
