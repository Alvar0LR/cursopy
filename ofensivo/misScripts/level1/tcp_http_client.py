#!/usr/bin/env python3


import socket
import sys
import argparse

# 🔹 PASO 1 — LEER ARGUMENTOS (Con argparse)
parser = argparse.ArgumentParser(description="Cliente HTTP básico usando Sockets TCP.")

# Añadimos los argumentos posicionales
parser.add_argument("host", help="El dominio o IP al que conectar (ej: example.com)")
parser.add_argument("port", type=int, help="El puerto del servidor (ej: 80)")

args = parser.parse_args()

host = args.host
port = args.port

# 🔹 PASO 2 — CREAR EL SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2.0)

try:
    # 🔹 PASO 3 — CONECTAR AL HOST
    print(f"--- Conectando a {host}:{port} ---")
    sock.connect((host, port))
    
    # 🔹 PASO 4 — PREPARAR EL MENSAJE
    # Construimos la estructura exacta del protocolo HTTP/1.1
    peticion = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    
    # 🔹 PASO 5 — ENVIAR DATOS
    sock.send(peticion.encode('utf-8'))

    # 🔹 PASO 6 — RECIBIR DATOS
    # Recibimos una cantidad razonable para ver las cabeceras y el inicio del HTML
    respuesta = sock.recv(4096)
    
    # 🔹 PASO 7 — MOSTRAR RESPUESTA
    print("--- Respuesta del servidor ---\n")
    print(respuesta.decode('utf-8', errors='ignore'))

except socket.timeout:
    print(f"Error: Tiempo de espera agotado conectando a {host}")
except ConnectionRefusedError:
    print(f"Error: El servidor en {host}:{port} rechazó la conexión")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # 🔹 PASO 8 — CERRAR SOCKET
    sock.close()
    print("\n--- Socket cerrado ---")
