import sys
import time
import Combinatoria

encontrado = False

def sin_numeros_repetidos(numero):
    caracteres = '0123456789'
    cadena = str(numero)
    for c in caracteres:
        if cadena.count(c) > 1:
            return False
    return True

def leer_cuadrados_sin_repeticion(archivo, longitud):
    resultado = list()
    with open(archivo, 'r') as archivo_cuadrados:
        for linea in archivo_cuadrados:
            cuadrado = linea.split(',')[1]
            if len(cuadrado) == longitud and sin_numeros_repetidos(cuadrado):
                resultado.append(cuadrado)
                #print(cuadrado)
    return resultado

def obtener_cuadrados(digitos, lista_cuadrados):
    resultado = list()
    for cuadrado in lista_cuadrados:
        if digitos in "".join(sorted(str(cuadrado))):
            resultado.append(cuadrado)
    return resultado


def main():
    inicio = time.clock()
    longitud = int(sys.argv[1])
    archivo_cuadrados = sys.argv[2]
    digitos = list()
    dicc_cuadrados = dict()
    for d in range(0,9):
        digitos.append(d)
    combinaciones = Combinatoria.combinaciones(digitos, longitud)
    lista_cuadrados = leer_cuadrados_sin_repeticion(archivo_cuadrados, longitud)
    lista_cuadrados.sort()
    global encontrado
    encontrado = False
    max_cuadrado = int()
    while not encontrado and lista_cuadrados:
        max_cuadrado = lista_cuadrados.pop()
        #print(max_cuadrado)
        digitos = "".join(sorted(str(max_cuadrado)))
        #print(digitos)
        if digitos not in dicc_cuadrados:
            cuadrados = obtener_cuadrados(digitos, lista_cuadrados)
            #print(cuadrados)
            if len(cuadrados) == 6: #7 cuadrados 
                encontrado = True
            else:
                dicc_cuadrados[digitos] = cuadrados
    print("--- Fin de ejecucion: %s segundos ---" % (time.clock() - inicio))
    if encontrado:
        print("Max. cuadrado: {}".format(max_cuadrado))
        print("Sus cuadrados: {}".format(cuadrados))

if __name__ == "__main__":
    main() 