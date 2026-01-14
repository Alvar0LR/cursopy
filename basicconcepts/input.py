#!/usr/bin/env python3

from getpass import getpass

condition = True

while condition:

	try:
		edad = int(input("Dime tu edad: "))
		print(f"Perfecto tienes {edad} años y el año que viene tendras {edad+1}")
		passwd = getpass("Introduce tu contraseña:")
		print(f"Tu contraseña es {passwd}")
		condition = False
	except ValueError:
		print("Error")
