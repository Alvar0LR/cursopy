#!/usr/bin/env python3

import os
from gestor import GestorNotas

def main():

    gestor = GestorNotas()
    while True:
        print("---MENU---\n")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opc = int(input(f"\n [+] Introduzca una opcion: "))

        if opc == 1:
            content=input(f"\n Introduce la nota: ")
            gestor.agregar_nota(content)
        elif opc == 2:
            notas=gestor.leer_notas()
            for i, nota in enumerate(notas):
                print(f"Nota - [{i}]: {nota}")
        elif opc == 3:
            texto = input("Ingresa el texto de la nota a buscar: ")
            nota = gestor.buscar_nota(texto)
            print(nota)
        elif opc == 4:
            indice = int(input(f"Introduce el indice de la nota a eliminar:"))
            gestor.borrar_indice(indice)
        elif opc == 5:
            print("Saliendo...")
            break
        else:
            print(f"\n [!] Esa opcion no existe")

        input(f"\n [+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
