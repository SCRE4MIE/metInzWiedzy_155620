import math
import numpy as np


def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b) ** 2
    return math.sqrt(wynik)


def metryka_euklidesowa_wektory_2(vector_1, vector_2, cut=False):
    if cut:
        vector_1 = np.delete(vector_1, len(vector_1)-1)
        vector_2 = np.delete(vector_2, len(vector_2)-1)

    dystans = vector_1 - vector_2
    return math.sqrt(np.dot(dystans, dystans))


vector1 = np.array([1,2,3])
vector2 = np.array([3,4,6])

print(metryka_euklidesowa_wektory([1,2, 3], [3,4, 6]))
print(metryka_euklidesowa_wektory_2(vector1, vector2, True))