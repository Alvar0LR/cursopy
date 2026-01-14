#!/usr/bin/env python3

class Calculadora: 
	def __init__(self, numero): #Calculadora.init(calc, numero)
		self.numero = numero # calc.numero = 5

	def suma(self, otro_numero): # Calculadora.suma(calc, otro_numero)
		return self.numero + otro_numero # calc.numero + otro_numero = 5 + 8 = 13

	def suma_doble(self, numero1, numero2): #Calculadora.suma_doble(calc, numero1, numero2)
		return self.suma(numero1) + self.suma(numero2) #calc.numero + numero1  +  calc.numero + numero2

calc = Calculadora(5)
print(calc.suma(8))
print(calc.suma_doble(2, 8))
