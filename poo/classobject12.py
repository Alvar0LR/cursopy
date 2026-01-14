#!/usr/bin/env python3

def mi_decorador(func):
	def envoltura():
		print("Envoltura del decorador ANTES de llamar a la funcion")
		func()
		print("Envoltura del decorador DESPUES de llamar a la funcion")
	return envoltura

@mi_decorador
def saludo():
	print("Hola estoy saludando dentro de la funcion")

saludo()
