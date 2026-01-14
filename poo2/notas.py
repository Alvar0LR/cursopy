#!/usr/bin/env python3

class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self):
        return f'''{self.contenido}'''
