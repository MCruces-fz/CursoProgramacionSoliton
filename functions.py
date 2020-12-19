import numpy as np
from const import *


def line(xmax: float) -> np.array:
    """
    Esta función genera lel array f

    Parameters
    ----------
    xmax : float
        DESCRIPTION. Este parametro res el tamaño máximo
        de la barra en la que vas a medir el campo

    Returns
    -------
    object
        DESCRIPTION.

    """
    f = np.zeros(n)
    for j in range(n):
        x = h * j
        f[j] = x / xmax
    return f


def exact(xmax):
    fexact = np.zeros(n)
    for j in range(n):
        x = h * j
        fexact[j] = np.tanh(x)
    return fexact


def sden_kink(i, f):
    if i == 0:
        df0 = (f[i + 1] - f[i]) / h
    elif i == n - 1:
        df0 = (f[i] - f[i - 1]) / h
    else:
        df0 = (f[i + 1] - f[i - 1]) / (2. * h)
    f0 = f[i]
    den0 = (.5 * df0 ** 2 + .5 * (1. - f0 ** 2) ** 2) * h
    return den0


def var_phi(ix, f):
    f0 = f[ix]
    # df0=(f[ix+1]-f[ix-1])/(2.0*h)
    d2f0 = (f[ix + 1] - 2. * f0 + f[ix - 1]) / (h ** 2)

    var0 = -2. * f0 * (1. - f0 ** 2) - d2f0

    return var0