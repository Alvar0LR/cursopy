#!/usr/bin/env python3

class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def __str__(self):
        return f'''Matricula: {self.matricula} --- Modelo: {self.modelo}
                Dispo: { 'Si' if self.disponible else 'No'}'''

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"El vehiculo con matricula {self.matricula} no se puede volver a alquilar")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"El vehiculo con matricula {self.matricula} no se puede devolver ya que no ha sido alquilado a nadie")

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        return self.vehiculos.append(vehiculo)


    def mostrar_vehiculos(self):
        return "\n".join([str(v) for v in self.vehiculos])

    def alquilar_vehiculo(self, matricula):
        condition = False
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
                print(f"Alquilado")
                print(f"{vehiculo}")
                condition = True
        if not condition:
           print(f"Ese vehiculo no existe")

    def devolver_vehiculo(self, matricula):
        condition = False
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()
                print(f"Devuelto")
                print(f"{vehiculo}")
                condition = True
        if not condition:
            print(f"Ese vehiculo no existe")



if __name__ == '__main__':

    flota = Flota()

    v1 = Vehiculo("3050-KVH", "Nissan")
    v2 = Vehiculo("2345-OLD", "Toyota")


    flota.agregar_vehiculo(v1)
    flota.agregar_vehiculo(v2)
    print("[I]---Vehiculos---[I]")
    print(flota.mostrar_vehiculos())
    print("[I]---Vehiculos Alquilados---[I]")
    flota.alquilar_vehiculo("3050-KVH")
    print("[I---Vehiculos Devueltos---[I]]")
    flota.devolver_vehiculo("3050-KVH")

