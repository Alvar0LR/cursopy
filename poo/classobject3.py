#!/usr/bin/env python3

class Rectangulo:

	def __init__(self, ancho, alto):
		self.ancho = ancho
		self.alto = alto

	@property
	def area(self):
		return self.ancho * self.alto

	def __str__(self):
		return f'''[+] Propiedades del rectangulo [Ancho: {self.ancho}] [Alto: {self.alto}]'''

	def __eq__(self, otro):
		return self.ancho == otro.ancho and self.alto == otro.alto

rect1 = Rectangulo(30, 40)
rect2 = Rectangulo(10, 60)
print(rect1.__str__())
print(rect1.area)
print(f"\n [+] Son iguales? -> {rect1 == rect2}")



