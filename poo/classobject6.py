#!/usr/bin/env python3

class Estudiantes():

	estudiantes = []

	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

		Estudiantes.estudiantes.append(self)

	@staticmethod
	def es_mayor_de_edad(edad):
		return edad >= 18

	@classmethod
	def crear_estudiante(cls, nombre, edad):
		if cls.es_mayor_de_edad(edad):
			return cls(nombre, edad)
			print(f"El estudiante {nombre} ha sido creado")
		else:
			print(f"El estudiante {nombre} no es mayor de edad")

	@staticmethod
	def mostrar_estudiantes():
		for i, estudiante in enumerate(Estudiantes.estudiantes):
			print(f"El estudiante {i+1} es {estudiante.nombre} y tiene {estudiante.edad}")

Estudiantes.crear_estudiante("Alvaro", 20)
Estudiantes.crear_estudiante("Alba", 14)
Estudiantes.crear_estudiante("Pedro", 20)
Estudiantes.crear_estudiante("Miguel", 16)
Estudiantes.crear_estudiante("Anotnio", 18)
Estudiantes.mostrar_estudiantes()
