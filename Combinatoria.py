
import time
import sys
import Queue
from math import factorial
import threading
import time
import os
import multiprocessing
from multiprocessing.dummy import Pool
from operator import itemgetter

def numero_combinaciones(m, n):
    """Calcula y devuelve el numero de combinaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // (factorial(n) * factorial(m - n))

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posicion i.
    """
    return lst[:i] + [x] + lst[i:]

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]



def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

def permutaciones(c, n=9):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])
#TODO clas worker
def obtener_primeros_de_conjuntos_en_paralelo(limites, threads):
    pool = Pool(threads)
    resultado = list()
    while not limites.empty(): 
        numeros = limites.get()
        resultado += pool.map(permutaciones, numeros)
        print("[{}]: Listo {}".format(threading.current_thread().getName(), numeros))
    
    #resultado.sort(key=itemgetter(2), reverse=True)
    pool.close()
    pool.join()
    return resultado

def main():
    inicio = time.clock()
    datos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cola = Queue.Queue()
    for item in datos:
        lista = list(datos)
        lista.remove(item)
        cola.put(lista)
        print(lista)
    for elem in list(cola.queue):
        print(elem)
    limite_inferior_original = int(sys.argv[1])
    limite_superior_original = int(sys.argv[2])
    cantidad_digitos = int(sys.argv[3])
    numero_threads = int(sys.argv[4])
    lista_resultados = obtener_primeros_de_conjuntos_en_paralelo(cola, numero_threads)
    print lista_resultados

    #lista_permutaciones = permutaciones(lista, cantidad_digitos)
    #TODO revisar
    for lista_numeros in lista_resultados:
        cifra_string = str()
        for numero in lista_numeros:
            cifra_string += numero
        cifra_int = int(cifra_string)
        if cifra_int >= limite_inferior_original and cifra_int <= limite_superior_original:
            lista_resultados.append(cifra_int)
    lista_resultados.sort()
    print lista_resultados
if __name__ == "__main__":
    main()  
