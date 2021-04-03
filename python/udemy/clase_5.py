
#clases y objetos
class ClaseSilla:
	color = "blanco"
	precio = 100

objetoSilla1 = ClaseSilla()
print(objetoSilla1.color) 
print(objetoSilla1.precio)


objetoSilla2 = ClaseSilla()
objetoSilla2.color = "verde"
objetoSilla2.precio = 50

print(objetoSilla2.color)
print(objetoSilla2.precio)


class Persona:
	#metodo constructor, self hace referencia a los atributos de la clase
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print("Hola, me llamo {} y tengo {} años".format(self.nombre,self.edad))


persona1 = Persona("Juan",27)
print(persona1.nombre)
print(persona1.edad)

persona1.saludar()


#funciones
def saludar():
	print("Buenos días a todos")


saludar()


def saludar(nombre):
	print(f"Buenos dias {nombre}")


nombre = "Jovannu"
saludar(nombre)


def sumar(num1,num2):
	return num1 + num2

num1 = 10
num2 = 20
print(sumar(num1,num2))

#paso de valor por referencia
#solo lo aplica aestructuras,listas,etc a cadenas y numeros no
def incluir_color(colores,color):
	colores.append(color)

color = "negro"
colores = ["verde","rojo","azul"]
incluir_color(colores,color)
print(colores)


print("\n")
#funcion lambda, funcion pequeña sin nombre

resultado = lambda numero : numero + 30

print(resultado(10))


resultado2 = lambda numero1, numero2 : numero1 + numero2
print(resultado2(40,40))




