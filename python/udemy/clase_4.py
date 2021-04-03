#condicionales
a = 5
b = 7

if a < b :
	print("a es menor que b")
elif a == b:
	print("a es igual que b")
else:
	print("A es mayo y diferente de b")


#bucle for
colores = ["rojo", "verde", "azul", "negro"]
for color in colores:
	print(color)

cadena = "Hola mundo"
for c in cadena:
	print (c)

print("\n")
for i in range(8):
	print(i)

for i in range(4):
	for n in range(3):
		print(i,n)


print("\n while")
#bucle while
valor = 1
fin = 10
while valor < fin:
	print(valor)
	valor += 1


print("\n")
#break
valor = 1
while valor < fin:
	if (valor == 5):
		break
	print(valor)
	valor += 1


print("\n")
#continue
valor = 0
while valor < fin:
	valor += 1
	if ((valor % 2)  == 0):
		continue;
	print(valor)

