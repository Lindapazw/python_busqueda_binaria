import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
        return -1

#  range(len(lista)) -> ,2,3,4,5 .... hasta len() -1 

miLista = [1,2,3,4,5,10,12]
print(busqueda_ingenua(miLista, 10))

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista)-1 # fin de la lista 

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2 