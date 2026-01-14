#!/usr/bin/env python3
from functools import reduce


print("---------------")
print("Funcion que no devuelve nada")
def saludo(nombre:str):
	print(f"\n Hola muy buenas {nombre}")

nombre = "Pepa"
saludo(nombre)
print("---------------")
print("Funcion que devuelve un valor")
def resta(x:int, y:int):
	resta=x-y
	return resta

numero1=8
numero2=6
operacion=resta(numero1, numero2)
print(f"\n{operacion}")

print("----------------")
print("funcion con lambda (anonima)")

miFuncion = lambda: "Hola Mundo"
print(miFuncion())

cubo = lambda x: x**3
print(cubo(7))


numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x : x**2, numeros))

print(cuadrados)

impares = reduce(lambda x, y: x*y, numeros)
print(impares)

print("-----------")
print("excepciones try")
try:
	int("Hola mundo")
except ValueError:
	print("Esto no tiene sentido")
