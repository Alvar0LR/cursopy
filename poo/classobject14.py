#!/usr/bin/env python3

print("---------args-------------")
def suma(*args):
	return sum(args)

print(suma(4,5,6,7,8,9))
print("-----------------------")

def presentacion(**kwargs):
	return kwargs

def listar_presentacion(**kwargs):
	for clave, valor in kwargs.items():
		if clave == "nombre":
			print(f"Para el nombre {kwargs['nombre']} tiene la profesion {kwargs['profesion']}, {kwargs.get('edad')}")

print(presentacion(nombre="Alvaro", profesion="Lammer", edad=20))
listar_presentacion(nombre="Jose", profesion="Informatico", edad=21)
