#!/usr/bin/env python3

import hashlib

def suma(x, y):
	return x + y

def resta(x, y):
	return x - y

def multi(x, y):
	return x * y

def division(x, y):
	if y < 0:
		print("No se puede dividir entre 0")
	else:
		return x / y


print(division(5,6))

print(hashlib.md5(b"sasa").hexdigest())

