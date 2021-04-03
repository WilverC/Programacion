

cifrad = ""
print("A continuación introduce un texto a cifrar")

texto = input("Texto: ")

pos = int(input("¿Cuántas posiciones deseas avanzar?: "))

#saber si el texto es mayusculas o minusculas
if texto == texto.upper():
	abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
	abc = "abcdefghijklmnñopqrstuvwxyz"

for c in texto:
	if c in abc:
		cifrad += abc[(abc.index(c))+pos%len(abc)]
	else:
		cifrad += c


print(f"Tu texto cifrado es {cifrad}")

text=""
print("Descifrar con las 27 posibilidades")
for n in range(1,27):
	for c in cifrad:
		if c in abc:
			text += abc[(abc.find(c) + n)%len(abc)]
		else:
			text += c
	print(f"Texto: {text}")
	text=""