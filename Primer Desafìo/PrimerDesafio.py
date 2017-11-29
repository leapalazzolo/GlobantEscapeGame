import sys
import time
import Combinatoria
from pycipher import Playfair


def eliminar_letras_repetidas(cadena):
    bandera = True
    #print(cadena)
    for i, letra in enumerate(cadena):
        #print(cadena.count(letra))
        if cadena.count(letra) > 1:
            bandera = False
            apariciones = [pos for pos, char in enumerate(cadena) if char == letra]
            print(letra, apariciones)
            if apariciones:
                for j in apariciones:
                    print(cadena[:j] + cadena[j+1:])
                    return eliminar_letras_repetidas(cadena[:j] + cadena[j+1:])
            return [] + [cadena]
    #if bandera:
            #continue
        #print(letra, i)
    

def main():
    inicio = time.clock()
    cifra = sys.argv[1]
    clave = sys.argv[2]
    print(clave)
    #lista_claves_parciales = eliminar_letras_repetidas("ELDESAFIOGLOBANT")
    lista_claves_parciales = eliminar_letras_repetidas(clave)
    print(lista_claves_parciales)
    #texto_plano = Playfair(clave).decipher(cifra)
    print("--- Fin de ejecucion: %s segundos ---" % (time.clock() - inicio))
    #print(texto_plano)
    #with open('resultado.txt') as archivo_resultado:
    #    archivo_resultado.write(texto_plano)

if __name__ == "__main__":
    main() 