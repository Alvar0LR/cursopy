#!/usr/bin/env python3

ports = [21, 22, 33, 44]
hackers= ["S4vitar", "Hackermate", "lobotec", "hackavis"]
more_hackers=["nate", "pilindris"]
another_ports = ports[0:9]
print(another_ports)

i = 0

while i<len(ports):
	print(ports[i])
	i+=1

for port, hacker in zip(ports, hackers):
	print(f"El puerto {port} le hace gracia al hacker {hacker}")


eliminado=hackers.pop(2)
print(f"El hacker {eliminado} a sido eliminado")
hackers.insert(2,"Chema Alonso")
hackers.extend(more_hackers)
hackers+=["Hola"]
hackers.remove("Hola")
hackers.append("Adios")
print(hackers)
