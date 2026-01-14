#!/usr/bin/env python3

class CuentaBancaria:
	def __init__(self, cuenta, nombre, dinero=0):
		self.cuenta = cuenta
		self.nombre = nombre
		self.dinero = dinero

	def depositar_dinero(self, dinero):
		self.dinero += dinero
		return f"[+] [{self.nombre}] Dinero añadido {dinero} ahora la cuenta tiene {self.dinero}"

	def retirar_dinero(self, dinero):
		if self.dinero < dinero:
			return f"[!] [{self.nombre}] No se puede retirar esa cantidad"
		else:
			self.dinero -= dinero
			return f"[-] [{self.nombre}] Cantidad retirada: {dinero} Cantidad restante {self.dinero} "


cuenta = CuentaBancaria("1893", "Antonio", 100)
print(cuenta.depositar_dinero(500))
print(cuenta.retirar_dinero(601))
