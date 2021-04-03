#Generar documentacion
#Docstrings

def saludar(nombre):
    """
    Esto será un comentario de la funcion saludar
    Esta función recibirá como parametro una cadena con el nombre
    e imprimirá por pantalla un saludo con el nombre concatenado
    """
    print(f"Buenos dias {nombre}")

saludar("Antonio")

help( saludar )


#pydoc ruta_del_fichero
#pydoc -w ruta_del_fichero crea un html de documentacion


#creacion de pruebas
def sumar(numero1, numero2):
    """
    Recibe dos numeros como parametros y devuelve su suma
    
    >>> sumar(4,3)
    7

    >>> sumar(5,4)
    9

    >>> sumar(1,3)
    7
    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()

#colocar lo siguiente para el doctest
#python archivo -v


#crear prueba dentro del mismo codigo
def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)

import unittest

class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(4,2), 8)

if __name__ == '__main__':
    unittest.main()