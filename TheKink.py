#!/usr/bin/env python
# coding: utf-8

# In[117]:


import numpy as np
import matplotlib.pyplot as mpl
import time as t

from functions import line, exact, sden_kink, var_phi

from const import *

mpl.close("all")


varf = np.zeros(n)


f = line(xmax)


fexact = exact(xmax)


energy = 0.0
for i in range(n):
    energy = energy + sden_kink(i, f)


for loop in range(loops):

    # Calcular variaciones
    for j in range(1, n - 1):
        varf[j] = var_phi(j, f)

    # Implementar variaciones
    for j in range(1, n - 1):
        f[j] = f[j] - delta * varf[j]

    if loop in prints:
        mpl.figure(0)  # (0 or loop)
        mpl.title(f"Iteración {loop}")
        mpl.xlabel("Espacio")
        mpl.ylabel("Campo")
        mpl.plot(f, label=f"iter. {loop}")
        mpl.legend(loc="best")
        mpl.show()


print(printing)
