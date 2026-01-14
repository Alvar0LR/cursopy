#!/usr/bin/env python3

class Calculadora:

	@staticmethod
	def suma(num1, num2):
		return num1 + num2

	@staticmethod
	def resta(num1, num2):
		return num1 - num2

	@staticmethod
	def multiplicacion(num1, num2):
	 	return num1 * num2

	@staticmethod
	def division(num1, num2):
		return num1 / num2 if num1 != 0 else f"El dividendo no puede ser 0 num = {num1}"

print(Calculadora.suma(2,6))
print(Calculadora.resta(2,4))
print(Calculadora.multiplicacion(3,6))
print(Calculadora.division(1,4))
