"""
    File with all global constants.
"""

n = 101  # Number of discrete points on space.
h = .1  # Size of each discrete space point.
loops = 10000  # Number of loops in the main loop.
xmax = (n - 1) * h  # Total length of the experiment.
delta = 1e-3  # Size of the diff.

# often = loops / 10  # Ten times per loop (unused already)
printing = loops / 5  # How often prints and plots on the main loop.
prints = [10, 100, 500, 1000, 9999]  # Number oftimes plotting results on the main loop.
