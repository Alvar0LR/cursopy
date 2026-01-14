#!/usr/bin/env python3

import pickle
from notas import Nota

class GestorNotas:
    def __init__(self, archivo_notas='notas.pkl'):
        self.archivo_notas = archivo_notas

        try:
            with open(self.archivo_notas, 'rb') as f:
                self.notas = pickle.load(f)

        except FileNotFoundError:
            self.notas = []

    def guardar_notas(self):
        with open(self.archivo_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
         self.notas.append(Nota(contenido))
         self.guardar_notas()

    def leer_notas(self):
        return self.notas

    def buscar_nota(self, texto):
        condition = False
        for nota in self.notas:
            if texto in nota.contenido:
                return nota
                condition = True
        if not condition:
            return f'''Nota no encontrada'''

    def borrar_indice(self, indice):
        if indice < len(self.notas):
            del self.notas[indice]
            self.guardar_notas()
            print(f"La nota con indice {indice} ha sido eliminada")
        else:
            print(f"\n [!] El indice proporcionado es incorrecto\n")
