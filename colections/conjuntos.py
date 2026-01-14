#!/usr/bin/env python3

mi_conjunto={1,2,3,4}
mi_conjunto.add(5)

print(mi_conjunto)

usuarios_facebook = {"Ana", "jose", "manolo", "Pepe"}
usuarios_x = {"Pepe", "Alvaro", "Alba", "Anotnio"}

ambas_plataformas = usuarios_facebook.intersection(usuarios_x)
union_plataformas = usuarios_facebook.union(usuarios_x)
diference_plataformas = usuarios_facebook.difference(usuarios_x)

print(ambas_plataformas)
print(union_plataformas)
print(diference_plataformas)

dic = {"nombre":"alvaro", "edad":20, "pais":"españa"}
print(dic)
