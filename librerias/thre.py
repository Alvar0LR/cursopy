#!/usr/bin/env python3

import multiprocessing
import time
import requests


#def tarea(num_tarea):
#    inicio = time.time()
#    print(f"\n [+] Hilo {num_tarea} iniciando {inicio}")
#    time.sleep(3)
#    print(f"\n [+] Hilo {num_tarea} finalizando {time.time() - inicio}")

#thread1 = threading.Thread(target=tarea, args=(1,))
#thread2 = threading.Thread(target=tarea, args=(2,))

#thread1.start()
#thread2.start()

#thread1.join()
#thread2.join()

#proceso1 = multiprocessing.Process(target=tarea, args=(1,))
#proceso2 = multiprocessing.Process(target=tarea, args=(2,))

#proceso1.start()
#proceso2.start()

#proceso1.join()
#proceso2.join()

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n [+] URL [{url}]: {len(response.content)} bytes")

dominios = [

    "https://google.es",
    "https://yahoo.com",
    "https://wikipedia.org"
]

start_time = time.time()

#for url in dominios:
#    respuesta = requests.get(url) 
#    print(f"La respuesta en B es {len(respuesta.content)} -> [{url}]")
#    print(f"{url} -> {respuesta.status_code}")
#print("\n [+] Las peticiones han finalizado correctamente")

procesos = []

for url in dominios:
    proceso = multiprocessing.Process(target=realizar_peticion, args=(url,))
    proceso.start()
    procesos.append(proceso)

for proceso in procesos:
    proceso.join()

end_time = time.time()

print(f"\n [+] Tiempo total transcurrido {round(end_time - start_time, 2)}")
