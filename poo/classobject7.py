#!/usr/bin/env python3

class Mascotas:

	mascotas = []

	def __init__(self, nombre, especie, edad):
		self.nombre = nombre
		self.especie = especie 
		self.edad = edad

		Mascotas.mascotas.append(self)

	@staticmethod
	def comprobar_requisitos(nombre, especie, edad):
		if not nombre or not especie:
			return False
		if edad < 18:
			return False

		return True
		#return bool(nombre and especie and edad >= 18 )
	@classmethod
	def crear_mascota(cls, nombre, especie, edad):
		if cls.comprobar_requisitos(nombre, especie, edad):
			return cls(nombre, especie, edad)
			print(f"La mascota a sido creada")
		else:
			print(f"La mascota {nombre} no a sido creada, [Datos incorrectos]")

	@classmethod
	def eliminar_mascota(cls, nombre):
		for mascota in Mascotas.mascotas:
			if mascota.nombre.lower() == nombre.lower():
				Mascotas.mascotas.remove(mascota)
				return f"La mascota con nombre: {mascota.nombre} ha sido eliminada"
			else: 
				return f"La mascota con nombre: {mascota.nombre} no ha sido eliminada"
	@staticmethod
	def mostrar_mascota():
		for i, mascota in enumerate(Mascotas.mascotas):
			print(f"La mascota [{i+1}] tiene como nombre {mascota.nombre}")

Mascotas.crear_mascota("pepe", "gato", 19)
Mascotas.crear_mascota("pepa", "perro", 20)
Mascotas.crear_mascota("gilig", "pajaro", 13)
Mascotas.mostrar_mascota()
print(Mascotas.eliminar_mascota("pepe"))
Mascotas.mostrar_mascota()

