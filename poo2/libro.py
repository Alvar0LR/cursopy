#!/usr/bin/env python3

class Libro:
    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        return f"ID: {self.id_libro}, Autor: {self.autor}, Libro: {self.nombre_libro}, Prestado: {self.esta_prestado}"


class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libros(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
        else:
            print(f"El libro con ID {libro.id_libro} ya existe en la biblioteca.")

    def buscar_id(self, id_busqueda):
        if id_busqueda in self.libros:
            print(self.libros[id_busqueda])
        else:
            print(f"No se encontró un libro con ID {id_busqueda}")

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"El libro esta prestado")

    def libros_prestados(self):
        for i, libro in self.libros.items():
            if libro.esta_prestado:
                print(i,libro)

    @property
    def mostrar_libros(self):
        for libro in self.libros.values():
            if not libro.esta_prestado:
                print(libro)


class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_para_n = {}

    def agregar_libros(self, libro, es_para_n):
        super().agregar_libros(libro)
        self.libros_para_n[libro.id_libro] = es_para_n

    def prestar_libro(self, id_libro, es_nino):
        if id_libro in self.libros and self.libros_para_n[id_libro] == es_nino and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"Ese libro no se puede prestar")

    def mostrar_libros_ninos(self):
        for i, libro in self.libros_para_n.items():
            if libro == True:
                print(i,libro)

if __name__ == '__main__':
    b = BibliotecaInfantil()

    libro = Libro(1, "Alvaro Lujan Ruiz", "El caballero de las sombras")
    libro2 = Libro(2, "Clara Soto Sanchez", "Ángel Caído")
    libro3 = Libro(3, "lili", "CocoXacamuelas")

    b.agregar_libros(libro, es_para_n=False)
    b.agregar_libros(libro2, es_para_n=False)
    b.agregar_libros(libro3, es_para_n=True)

    print("\n📚 Lista de libros en la biblioteca:\n")
    b.mostrar_libros

    print("\n Buscar por Id de libro")
    b.buscar_id(1)

    print("\n Libros sin prestar ")
    b.prestar_libro(1, es_nino=False)
    b.prestar_libro(3, es_nino=True)
    b.mostrar_libros
    print("\n Libros prestados")
    b.libros_prestados()
    print("\n Libros para niños")
    b.mostrar_libros_ninos()
