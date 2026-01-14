#!/usr/bin/env python3

example = (1, "test", [1, 2, 3], 4, True, {'Manzanas': 1, 'peras' : 5}, 5)
print(example)

mi_tupla=(1,2,3,4)
a,b,c,d=mi_tupla
print(a)
print(b)
print(c)
print(d)
print("---")
print(len(mi_tupla))

tercera_tupla= mi_tupla + example
print(tercera_tupla)

res = tuple(i for i in mi_tupla if i % 2 == 0)
print(res)


