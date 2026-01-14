#!/usr/bin/env python3

class Persona: 
	def __init__(self, nombre, edad): 
		self.nombre = nombre
		self.edad = edad

	def saludo(self):
		return f'''Hola me llamo {self.nombre}, tengo {self.edad}'''



class Programador(Persona):
	def __init__(self, nombre, edad, salario):
		super().__init__(nombre, edad)
		self.salario = salario

	def saludo(self, hobbie):
		return f'''{super().saludo()} {hobbie}  y gano {self.salario} al año'''
	
persona = Persona("Sancho", 20)
print(persona.saludo())

programador = Programador("Alvaro", 23, 1100)
print(programador.saludo("Gym"))

