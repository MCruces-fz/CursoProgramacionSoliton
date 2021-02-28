"""
    F U N C T I O N   D E F I N I T I O N S

    Here are defined all functions used in other scripts.
"""
import numpy as np
from const import *


def line(xmax: float) -> np.array:
    """
    This funciton generates the f array. This is the initial guess (a discretized straight line).

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
    den0 = (.5 * df0 ** 2 + .5 * (1. - f0 ** 2) ** 2) * h  # Density
    return den0


def sden_hdhg(i: int, f: np.array) -> float:
    """
    Energy Density
    """
    f0 = f[i]
    if i == 0:
        df0 = (f[i + 1] - f[i]) / h
        d2f0 = (f[i + 2] + f[i] - 2 * f[i + 1]) / (2 * h ** 2)
    elif i == n - 1:
        df0 = (f[i] - f[i - 1]) / h
        d2f0 = (f[i - 2] + f[i] - 2 * f[i - 1]) / (2 * h ** 2)
    else:
        df0 = (f[i + 1] - f[i - 1]) / (2. * h)
        d2f0 = (f[i + 1] - 2. * f0 + f[i - 1]) / (h ** 2)
    # r = h * (i + .5)
    r = i / 100 * 15
    # FIXME: escribir la densidad de energía
    #  pág. 17 (hecho)
    # den0 = 1 / (3 * np.pi) * (
    #             r ** 2 * df0 ** 2 + 2 * np.sin(f0) ** 2 * (1 + df0 ** 2) + np.sin(f0) ** 4 / r ** 2)  # Density
    x = r
    df = df0
    ddf = d2f0
    den0 = (x**2*df**2 + 2*np.sin(f)**2*(1 + df**2) + np.sin(f)**4/(x**2))/(3*np.pi)
    print(f"f0: {f0:.3f}, df0: {df0:.3f}, d2f0: {d2f0:.3f}, den0: {den0:.3f}")
    return den0


def var_phi(ix: int, f: np.array) -> float:
    """
    This function yields the variation of the field in each point that follows the gradient of the energy
    """

    f0 = f[ix]

    # This is the second derivative of the field (phi) at the point
    d2f0 = (f[ix + 1] - 2. * f0 + f[ix - 1]) / (h ** 2)

    var0 = -2. * f0 * (1. - f0 ** 2) - d2f0  # Euler Lagrange
    return var0


def var_hdg(i: int, f: np.array) -> float:
    """
    Variation of the energy functional
    """
    # TODO: cambiar ix  -> i (hecho)

    r = h * (i + .5)
    f0 = f[i]
    df0 = (f[i + 1] - f[i - 1]) / (2.0 * h)
    d2f0 = (f[i + 1] - 2. * f0 + f[i - 1]) / (h ** 2)
    # var0 = 2 / (3 * np.pi) * (np.sin(2 * f0) * (1 - df0 ** 2) + np.sin(2 * f0) * np.sin(
    #     f0) ** 2 / r ** 2 - 2 * r * df0 - r ** 2 * d2f0 - 2 * np.sin(f0) ** 2 * d2f0)  # Euler Lagrange

    x = i / 100 * 15
    df = df0
    ddf = d2f0
    var0 = -2 * ((x ** 2 + 2 * np.sin(f) ** 2) * ddf + 2 * x * df + np.sin(2 * f) * (
                df ** 2 - 1 - np.sin(f) ** 2 / (x ** 2))) / (3 * np.pi)
    return var0
