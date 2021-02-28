
#!/usr/bin/env python
# coding: utf-8
"""
  T H E   G R A D I E N T   F L O W   M E T H O D

  This is the main program to use the gradient flow method for a Kink.
"""

import numpy as np
import matplotlib.pyplot as mpl


from functions import line, sden_hdhg, var_hdg

from const import *

mpl.close("all")


varh = np.zeros(n)

# Arrays with initial information about the simulation
f = np.array([np.pi*(1 - r/(n-1)) for r in range(n)])
# mpl.plot(f)
# print(f)
# fexact = *******

# Discrete integral of the energy in the whole system.
energy = 0.0
for i in range(n):
    energy = energy + sden_hdhg(i, f)

for loop in range(loops):

    # Calculation of variations
    for j in range(1, n - 1):
        varh[j] = var_hdg(j, f)

    # Implementation of variations
    for j in range(1, n - 1):
        f[j] = f[j] - delta * varh[j]
    if loop in prints:
        mpl.plot(f)
        mpl.show()
    continue

    # if statement for plot information
    if loop in prints:
        mpl.figure(2)  # (0 or loop)
        mpl.title(f"Iteración {loop}")
        mpl.xlabel("Espacio")
        mpl.ylabel("Campo")
        mpl.plot(f, label=f"iter. {loop}")
        mpl.legend(loc="best")
        mpl.show()
