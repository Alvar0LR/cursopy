#!/usr/bin/env python

class Automovil:

	automoviles = []

	def __init__(self, matricula, *piezas):
		self._matricula = matricula
		self._piezas = list(piezas)

	def agregar_auto(self):
		Automovil.automoviles.append(self)

	@classmethod
	def eliminar_auto(cls, matricula):
		encontrado = False
		for auto in cls.automoviles:
			if auto._matricula == matricula:
				cls.automoviles.remove(auto)
				print(f"Auto: {auto._matricula} eliminado")
				encontrado = True
		if not encontrado:
			print(f"Auto: {matricula} no encontrado")

	@classmethod
	def encontrar_coche_matricula(cls, matricula):
		encontrado = False
		for auto in cls.automoviles:
			if auto._matricula == matricula:
				print(f"Matri {auto._matricula} | Piezas {', '.join(auto._piezas)}")
				encontrado = True
			if not encontrado:
				print(f"Auto no encontrado")

	@classmethod
	def listar_autos(cls):
		if not cls.automoviles:
			print("No hay automoviles")
			return
		for i, auto in enumerate(cls.automoviles, start=1):
			print(f"[{i}] Matricula -> {auto._matricula} | Piezas {', '.join(auto._piezas)}")

auto = Automovil("4543-KWX", "Motor-lambo", "4ruedas", "frenos")
auto2 = Automovil("4542-KWS", "Motor-lambo", "4ruedas", "frenos")

auto.agregar_auto()
auto2.agregar_auto()
auto2.eliminar_auto("4543-KWX")
auto.encontrar_coche_matricula("4542-KWS")
Automovil.listar_autos()
