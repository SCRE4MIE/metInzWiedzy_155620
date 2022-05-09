import numpy as np


def f(x):
    return x


def montecarlo(func, a, b, n):
    shots_x = np.random.uniform(a, b, n)
    shots_y = [func(val) for val in shots_x]
    shots_y_mean = np.sum(shots_y)/n
    return (b-a) * shots_y_mean


print(montecarlo(f, 0,1, 1000))
