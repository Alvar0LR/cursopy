#!/usr/bin/env python3

class Cuentabancaria:

	def __init__(self, num_cuenta, titular, saldo_inicial=0):
		self.num_cuenta = num_cuenta
		self.titular = titular
		self.__saldo = saldo_inicial

	def depositar_dinero(self, saldo):
		if saldo > 0:
			self.__saldo += saldo
			return self.__saldo
		else:
			return f'''[ERROR] Introduce una cantidad de dinero mayor que 0$'''

	def retirar_dinero(self, saldo):
		if saldo > 0:
			if self.__saldo < saldo:
				return f'''Estas a 0$, no puedes sacar dinero'''
			else:
				self.__saldo -= saldo
				return self.__saldo

	def __str__(self):
		return f'''{self.num_cuenta} | {self.titular} | {self.__saldo}'''



cuenta = Cuentabancaria(1, "Alvaro", 5)
print(cuenta)

print(cuenta.depositar_dinero(50))
print(cuenta.retirar_dinero(50))

