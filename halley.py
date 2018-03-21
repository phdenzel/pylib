#!/usr/bin.env python
"""
@author: phdenzel

Calculate comet Halley's theoretical trajectory
"""
import numpy as np
import matplotlib.pyplot as plt
from raphson_root import newton_raphson


a = 17.8
e = 0.967

def kepler(E, M, e):
    """
    Kepler's equation
    """
    return E - e*np.sin(E) - M


def dkepler(E, M, e):
    """
    Derivative of Kepler's equation
    """
    return 1 - e*np.cos(E)


def elliptical_xy(E, e, a):
    """
    Convert E coordinates into x, y coordinates
    """
    x = a * (np.cos(E) - e)
    y = a * (np.sqrt(1-e*e)*np.sin(E))
    return x, y


def halley_trajectory(e, a, Nsteps=150):
    """
    Calculate Halley's trajectory
    """
    M = np.linspace(0, 2*np.pi, Nsteps)
    x, y = [], []
    for m in M:
        E0 = newton_raphson(kepler, 5, df=dkepler, M=m, e=e)
        x0, y0 = elliptical_xy(E0, e, a)
        x.append(x0)
        y.append(y0)
    return x, y


if __name__ == "__main__":
    x, y = halley_trajectory(e, a, 300)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color="#ff3366", lw=0, marker='.')
    ax.set_aspect('equal')
    plt.show()
