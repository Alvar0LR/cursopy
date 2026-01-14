#!/usr/bin/env python3

import requests

#response = requests.get("https://google.es")

#print(f"\n[+] Codigo de Respuesta: {response.status_code}")
#print(f"\n[+] Mostrando codigo fuente de la respuesta:\n")

#with open("index.html", "w") as f:
#    f.write(response.text)

###GET###
#payload = {'key':'value', 'ke2':'value2'}
#response = requests.get("https://httpbin.org/get", params=valus)
#print(f"\n[+] URL: {response.url} \n")
#print(f"\n[+]{response.text}")

###POST###
#response = requests.post("https://httpbin.org/post", data=payload)
#print(response.text)

###GET-HEADERS###
#header = {'User-Agent': 'Se tensa'}

#response = requests.get('https://google.es', headers=header)
#print(response.request.headers)

###GET-TIMEOUT###
#try:
#    response = requests.get("https://google.es", timeout=1)
#    response.raise_for_status()

#except requests.Timeout:
#    print(f"\n[!] La peticion ha excedido el limite de su tiempo de espera")
#except requests.HTTPError as http_err:
#    print(f"\n[!] Error HTTP: {http_err}")
#except requests.RequestException as err:
#    print(f"\n{err}")
#else:
#    print(f"\n[+] No ha habido ningun error")

response = requests.get("https://httpbin.org/get")
data = response.json()

if 'headers' in data and 'User-Agent' in data['headers']:
    user_agent = data['headers']['User-Agent']
    print(f"\n[+] User-Agent {user_agent}")
else:
    print(f"\n[!] No existe este campo en la respuesta")
