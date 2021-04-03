#Operadores aritméticos
suma = 10 + 5
print(suma)

resta = 10 - 8
print(resta)

multi = 10 * 3
print(multi)

div = 10 / 2
print(div)

resto = 10 % 3
cociente = 10 // 3
print(f"cociente {cociente} resto {resto}")

exp = 2 ** 3
print(exp)

#Operadores de asignacion
numero = 5
print(numero)

numero += 4 
print(numero)

numero -= 3
print(numero)

numero *= 2
print(numero)

numero /= 6
print(numero)

numero **= 3
print(numero)

#Operadores de comparación
numero1 = 5
numero2 = 6

print("Igual")
print(numero1 == numero2)
print("diferente")
print(numero1 != numero2)
print("menor que")
print(numero1 < numero2)
print("mayor que")
print(numero1 > numero2)
print("mayor que o igual")
print(numero1 >= numero2)
print("menor que o igual")
print(numero1 <= numero2)

#Operadores lógicos
num1 = 10
num2 = 7
num3 = 5
num4 = 8

print((num1 > num3) and (num3 < num4))
print((num1 < num3) or (num3 < num4))
print(not((num1 > num3) or (num3 < num4)))

#Operadores de identidad
frutas1 = ["manzanas","peras"]
frutas2 = ["manzanas","peras"]
frutas3 = frutas1

print("frutas3 es fruta1")
print(frutas3 is frutas1)

frutas3.append("naranjas")

print("frutas3 no es fruta2")
print(frutas3 is not frutas2)

#operadores de permanencia
frutas1 = ["manzanas","peras","naranjas"]
frutas2 = "peras"

print("Esta frutas2 en frutas1")
print(frutas2 in frutas1)

print("No esta frutas2 en frutas1")
print(frutas2 not in frutas1)
