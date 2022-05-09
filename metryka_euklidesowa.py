import math


def metryka_euklidesowa(listaA, listaB):
    wyniki = 0
    for i in range(len(listaA)-1):
        wyniki += (listaA[i]-listaB[i])**2
    return math.sqrt(wyniki)
