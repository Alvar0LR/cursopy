#!/usr/bin/env python3

import time

def cronometro(func):
	def envoltura():
		inicio = time.time()
		func()
		final = time.time()

		res = inicio - final 
		print(f"La duracion {func.__name__}: {res}")
	return envoltura


@cronometro
def pausa_corta():
	time.sleep(1)
@cronometro
def pausa_larga():
	time.sleep(2)


pausa_corta()
pausa_larga()

