"""
Comandos que no interpreta

print( "hola" ) #comentario
print( "Profe" )

#variables
v_texto = " Estamos en "
year = 2021
pi = 3.1416
print( v_texto + " el año: " + str(year) )

nacio = input( "En que año nacio: ")
edad = ( year -int(nacio) )
print("En 2021 cumples "+ str(edad) + " años" )

#condicionales
if edad >= 18:
    print("Eres Mayor de 18 años")
else:
    print("Eres menor de edad")


#funciones
def circulo():
    radio = float( input("Radio en cm: ") )
    area = pi * (radio * radio)
    print( "Area= " + str(area) + "cm")
    perimetro = 2 * radio * pi
    print( "Perimetro= " + str(perimetro) + "cm")

circulo()

v_numero = int( input("numero a elevar: ") )
def cuadrado( numero ):
    resultado = 0
    resultado = numero * numero
    print( "Elevado al cuadrado es = " + str(resultado) )

cuadrado( v_numero )

"""
"""
Listas
metas = ["Hijo", "Arbol", "Viajar", "Canal_100k", "E_Empresa"]
print( metas )
print( metas[2] )

for info in metas:
    print( info )

print( type( metas ) )
"""

#tuplas

#diccionarios


"""
inicio = 1
fin = 6

while inicio < fin:
    print(f"Esta es la fila {inicio}")
    inicio = inicio + 1
"""

"""
class Coche:
    def __init__ (self, marca, color, combustible, cilindrica):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrica = cilindrica

    def mostrar_caracteristicas(self):
        print(f"marca {self.marca}")
        print(f"color {self.color}")
        print(f"combustible {self.combustible}")
        print(f"cilindrica {self.cilindrica}")

c = Coche("Opel", "rojo", "gasolina", "1.6")
c.mostrar_caracteristicas()

media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3
resul = media(4,6,5)
print(resul)
"""
