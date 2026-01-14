#!/usr/bin/env python3

import os

# def validar_correo(correo):

#    patron = "[A-Za-z0-9._+-]@[A-Za-z0-9]+\.[A-Za-z]{2,}"
#    if re.findall(patron, correo):
#        return True
#    else:
#        return False

# print(validar_correo("soporte@hack4u.io"))


#for i in range(1,6):
#    ruta = f"directorio/archivo{i}.txt"
#    if not os.path.exists(ruta):
#        open(ruta, "a").close()
#        print("Los archivos ya existen")
#    else:
#        print("Los archivos ya existian")

#if os.path.exists("directorio/archivo2.txt"):
#    os.remove("directorio/archivo2.txt")
#    print("Archivo eliminado")

#ruta = "directorio/archivo1.txt"
#if os.path.exists(ruta):
#    os.rename("directorio/archivo1.txt", "directorio/file1.txt")

ruta = os.path.join("directorio", "file1.txt")
print(f"\n [+] La ruta es: {ruta} \n")
# nombre_archivo = os.path.basename(ruta) = file.txt
# nombre_directorio = os.path.dirname(ruta) = directorio

#directorio, archivo = os.path.split(ruta)
#print(f"Archivo: {archivo}, Directorio: {directorio}")
