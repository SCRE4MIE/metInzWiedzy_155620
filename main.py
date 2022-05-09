import math

def load_file(file):
    array = []
    with open(file, 'r') as f:
        for line in f:
            row = [elt.rstrip('\n') for elt in line.split(' ')]
            array.append(row)
    return array


def load_file_2(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(line.replace('\n', '').split())
    return lista


def load_file_3(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista


def metryka_euklidesowa(listaA, listaB):
    wyniki = 0
    for i in range(len(listaA)-1):
        wyniki += (listaA[i]-listaB[i])**2
    return math.sqrt(wyniki)


# Praca domowa
def pracadomowa(lista):
    list_0 = []
    list_1 = []
    list_idx_0 = lista[0]
    for i in range(1, len(lista)):
        metryka_eukl = metryka_euklidesowa(list_idx_0, lista[i])
        if lista[i][len(lista[0])-1] == 0:
            list_0.append(metryka_eukl)
        elif lista[i][len(lista[0])-1] == 1:
            list_1.append(metryka_eukl)
    dictionary = {
        '0': list_0,
        '1': list_1,
        }
    return dictionary

# arr = load_file('australian.dat')
# arr2 = load_file_2('australian.dat')
# print(arr)
# print(arr2)

arr3 = load_file_3('australian.dat')
print(pracadomowa(arr3))
print(len(arr3))
# print(arr3)
# print(metryka_euklidesowa(arr3[0], arr3[1]))
