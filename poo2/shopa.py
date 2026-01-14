#!/usr/bin/env python3

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def __str__(self):
        return f'''\n Animal: {self.nombre}, Especie: {self.especie}

        -> Alimentado: {'Si' if self.alimentado else 'No'} \n'''

    def alimentar(self):
        self.alimentado = True
    def vender(self):
        self.alimentado = False

class TiendaAnimales:

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        return "\n".join([str(animal) for animal in self.animales])

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        condition = False
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                print(f"{animal}")
                self.animales.remove(animal)
                condition = True
        if not condition:
            print("Este animal ya ha sido vendido")

if __name__ == '__main__':

    tienda = TiendaAnimales("SHOPA")


    gato = Animal("Juan", "Gato")
    perro = Animal("Noa","Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    tienda.alimentar_animales()
    print("[O]---Animales vendidos---[O]\n")
    tienda.vender_animal("Jua")
    print("[I]---Animales de la tienda---[I]\n")
    print(tienda.mostrar_animales())




