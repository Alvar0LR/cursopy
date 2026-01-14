#!/usr/bin/env python3

import os

directorio_actual = os.getcwd()

print(f"\n[+] Directorio actual de trabajo: {directorio_actual}")

files = os.listdir(directorio_actual)

print(f"\n[+] Listando los archivos existentes en el directorio actual: {directorio_actual}:\n")

for f in files:
    print(f)

if not os.path.exists("mi_directorio"):

    os.mkdir("mi_directorio")

    print(f"\n[+] Directorio 'mi_directorio' creado:\n ")

    files = os.listdir(directorio_actual)

    for f in files:
        print(f)

print(f"\n[+] El directorio existe el archivo 'mi_archivo' -> {os.path.exists('os.py')}")
