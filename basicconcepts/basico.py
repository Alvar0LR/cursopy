#!/usr/bin/env python3

v = "192.168.1.189"
print(v)
print("---------------")
lis=["22","89"]
lis.append("40")
lis.remove("22")
del lis[1]
print(lis[0])
lis.append("50")
lis.append("99")
print("--------------------------")
for i in range(len(lis)):
	print(f"Puertos {i}: -> {lis[i]}")

print("-----------------------")
for i, u in enumerate(lis):
	print(f"{i}: {u}")
print("-----------------------")
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

result = map(sum, zip(odd_numbers, even_numbers))
for i in result:
	print(i)

print("-------------------------")

nombre =  "draygon"
rol = "estudiante"
edad = 20

print("Hola mi nombre es %s y mi rol es %s y tengo %d años" % (nombre,rol,edad))
print("Hola mi nombre es {}! y mi rol es {} y tengo {} años".format(nombre,rol,edad))
print(f"Hola mi nombre es {nombre} y mi rol es {rol} y tengo {edad} años")

tupla = ([1,2,3])
print(tupla)
print(even_numbers[2])
