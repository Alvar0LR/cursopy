#!/usr/bin/env python3  

for i in range(5): 
	print(i)

my_list = [[1, 2, 3], [4, 5, 6], [9, 4, 1]]
print("-------------------")
print("for anidado")
for element in my_list:
	print(f"\n [+] Vamos a desglosar la lista {element}")
	for my_list_element in element:
		print(my_list_element)

print("------------")
print("ternario bucle + lista")
odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)

print("-----------------")
print("for + if")
for i in range(10):
	if i == 5:
		print(f"[+] {i}")
	else:
		print(f"[-] {i}")

print("--------------------")
print("While + if")
i = 0
while i < 6:
	if i == 5:
		print(f"[+] {i}")
		break
	i += 1
else:
	print("Concluimos el bucle de forma exitosa")

print("-----------------------")
print("condicional ternario")
edad = 20
mensaje = "[+] Eres un adulto" if edad >= 18 else "[-] Eres menor de edad"
print(mensaje)

print("---------------------")
numbers = [1, 2, 3, 5, 56, 89, 78]
print("!= / or")
for num in numbers:
	if num % 2 != 0 or num == 2:
		print(f"[+] El numero es impar o 2 {num}")
	else:
		print(f"[-] El numero es par {num}")

print("--------------")
print("and")
amigos = ["roberto", "carlos", "lucia"]
casa = "guadalupe"

for amigo in amigos: 
	if amigo == "roberto" and casa == "guadalupe":
		print(f"ese es robiwobins {amigos[0]}")
	elif amigo == "carlos" or casa == "murcia":
		print(f"ese es el carlicos {amigos[1]}")
	elif amigo == "lucia" or casa == "javali":
		print(f"lucipuxisss {amigos[2]}")
	else: 
		print("ya")



