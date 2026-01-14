#!/usr/bin/env python3

import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"\n[+] Total de argumentos que se estan pasando al programa: {len(sys.argv)}")
print(f"\n[+] Mostrando todos los argumentos: {','.join(argument for argument in sys.argv)}")

for element in sys.path:
    print(element)


print(f"\n[+] Saliendo con un codigo de estado 0 (existoso)")
sys.exit(0)
