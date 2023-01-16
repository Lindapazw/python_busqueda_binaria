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