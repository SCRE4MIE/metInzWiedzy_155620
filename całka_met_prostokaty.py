import numpy as np


def rectangle(low, hight, f, n):
    edges = np.linspace(low, hight, n)
    area = 0
    for r in range(len(edges)):
        area += f(low + r*(hight-low)/n)*(hight-low)/n
    return area


def trig(x):
    return x


print(rectangle(0,1,trig, 100000))