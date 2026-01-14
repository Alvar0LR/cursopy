#!/usr/bin/env python3

class Libro:
	IVA = 0.21

	def __init__(self, titulo, autor, precio):
		self.titulo = titulo
		self.autor = autor
		self.precio = precio

	@staticmethod
	def es_bestseller(titulo, total_ventas):
		if total_ventas > 500:
			return f"Tu libro [{titulo}] es bestseller tiene {total_ventas} ventas"
		else:
			return f"Tu libro [{titulo}] no es bestseller tiene {total_ventes} ventas"

	@classmethod
	def precio_con_iva(cls, precio):
		return precio + precio * cls.IVA

class LibroDigi(Libro):
	IVA = 0.10

libro = Libro("El sutil Arte de que casi todo te importe una mierda", "Mark Marquez", 18.59)
libro_digi = LibroDigi("Habitos atomicos", "mark mason", 14.99)

print(libro.es_bestseller("El sutil Arte de que casi todo te importe una mierda",900))
print("------------")
print(libro.titulo)
print("------------")
print(f"El libro applicando el iva se queda en {Libro.precio_con_iva(libro.precio)}")
print(f"El libro applicando el iva se queda en {LibroDigi.precio_con_iva(libro_digi.precio)}")
