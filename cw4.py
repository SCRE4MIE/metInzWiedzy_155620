from load_file import load_file_3
from metryka_euklidesowa import metryka_euklidesowa
from collections import defaultdict


def foo(x, lista):
    list_0 = []
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0])-1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        list_0.append((klasa_decyzyjna, odleglosc))
    return list_0


def foo_pogrupowane(x, lista):
    slownik = defaultdict(list)
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0])-1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        slownik[klasa_decyzyjna].append(odleglosc)
    return slownik


def KNM(x, lista, k):
    slownik = defaultdict(list)
    slownik_finalny = {}
    for i in range(len(lista)):
        klasa_decyzyjna = (lista[i][len(lista[0])-1])
        odleglosc = metryka_euklidesowa(x, lista[i])
        slownik[klasa_decyzyjna].append(odleglosc)
    for key in slownik:
        suma = 0
        slownik[key].sort()
        for i in range(k):
            suma += slownik[key][i]
        slownik_finalny[key] = suma
    return slownik_finalny


arr = load_file_3('australian.dat')
# print(arr)
# print(foo([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], arr))
# print(foo_pogrupowane([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], arr))
print(KNM([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], arr, 5))
