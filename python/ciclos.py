'''
*
*Autor: Jovanny Wilver Cortez Enriquez
*Descripción: Ciclos
'''

'''------Ciclo For------'''
#sintaxis
#for (variable) in (limite o rango):

#tabla de multiplicar del 10 con for
print("tabla de multiplicar del 10 con for")
for i in range(10):
	res = 10 * i
	print("10 * {} = {}".format(i,res))

#tabla de multiplicar del 10 con for
print("tabla de multiplicar del 10 con while-----")
j = 0
while j < 10:
	res = 10 * j
	print("10 * {} = {}".format(j,res))
	j += 1

'''--------for en listas-----------'''
#recorre la lista elemento tras elemento 
lista = ["A", "B", "C"]
for elemento in lista:
	print(elemento)

''' ------- Ciclo While ----------'''
print("--------aumentar numero ----------------")
num_ac = 1
#sintexis
# while (condicion):

while num_ac <= 5:
	print(num_ac)
	num_ac += 1

#terminar el while con variable

prompt = "\nDime algo y lo repito"
prompt += "\ningresa 'salir' para salir del programa: "

msj = ""

while msj != "salir":
	msj = input(prompt)
	print(msj)


#romper el while con break
prompt = "\nDime algo y lo repito"
prompt += "\ningresa 'salir' para salir del programa: "

while True:
	opcion = input(prompt)
	
	if(opcion == 'salir'):
		break
	else:
		print("\nLe sirvo su comida "+opcion.title()+"!")


#valor continue
num = 0
while num <= 10:
	num += 1
	if(num % 2 == 0):
		continue

	print(num)



