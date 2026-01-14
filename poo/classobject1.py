#!/usr/bin/env python3

class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def saludo(self):
		return f"Hola soy {self.nombre} y tengo {self.edad}"


persona = Persona("Marcelo", 28)
persona2 = Persona("Juan", 20)
print(persona.saludo())
print(persona2.saludo())


