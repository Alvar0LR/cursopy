#!/usr/bin/env python3

dic = {"nombre":"alvaro", "edad":20, "pais":"españa"}
dic["nombre"] = "pedro"
dic["region"] = "murcia"

print("----------------")
print(dic.get("nombre"))
print(dic)

print("----------------")
del dic["region"]
print(dic)

print("----------------")

if "nombre" in dic:
	print("Esta clave existe")
else:
	print("Esta clave no existe")

print("------------")
for key, value in dic.items():
	print(f"{key} - {value}")

