"""
    F U N C T I O N   D E F I N I T I O N S

    Here are defined all functions used in other scripts.
"""
import numpy as np
from const import *


def line(xmax: float) -> np.array:
    """
    This funciton generates the f array

    Parameters
    ----------
    xmax : float
        DESCRIPTION. 
        This parameter is the maximum size of the
        bar (experiment/simulation) where we will 
        measure the field.

    Returns
    -------
    object
        DESCRIPTION.
        Array with initial field values.
    """

    f = np.zeros(n)
    for j in range(n):
        x = h * j
        f[j] = x / xmax
    return f


def exact(xmax: float) -> np.array:
    """
    This function generates the fexact array.

    Parameters
    ----------
    xmax : float
        DESCRIPTION. 
        This parameter is the maximum size of the
        bar (experiment/simulation) where we will 
        measure the field.

    Returns
    -------
    object
        DESCRIPTION.
        Array with initial field values for the exact
        expected field.

    """

    fexact = np.zeros(n)
    for j in range(n):
        x = h * j
        fexact[j] = np.tanh(x)
    return fexact


def sden_kink(i: int, f: np.array) -> float:
    """
    This function returns the value of the field
    on each discrete point of the space, AKA field
    density.

    Parameters
    ----------
    i:  integer
        DESCRIPTION. 
        Index of the position of the discrete point.

    f : numpy array 
        DESCRIPTION. 
        Array with initial conditions.

    Returns
    -------
    float
        DESCRIPTION.
        Array with initial field values for the exact
        expected field.
    """

    if i == 0:
        df0 = (f[i + 1] - f[i]) / h
    elif i == n - 1:
        df0 = (f[i] - f[i - 1]) / h
    else:
        df0 = (f[i + 1] - f[i - 1]) / (2. * h)
    f0 = f[i]
    den0 = (.5 * df0 ** 2 + .5 * (1. - f0 ** 2) ** 2) * h
    return den0


def var_phi(ix: int, f: np.array) -> float:
    """
    I don't remember what's this...
    """

    f0 = f[ix]
    # df0=(f[ix+1]-f[ix-1])/(2.0*h)
    d2f0 = (f[ix + 1] - 2. * f0 + f[ix - 1]) / (h ** 2)

    var0 = -2. * f0 * (1. - f0 ** 2) - d2f0
    return var0
