#!/usr/bin/env python3

import socket

def start_server():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host,port))
        print(f"\n [+] Servidor en escucha en {host}:{port}")
        s.listen(1)
        conection, address = s.accept()

        with conection:
            print(f"\n [+] Se ha conectado un nuevo cliente: {address}")
            while True:
                data = conection.recv(1024)
                print(f"\n [+] La data del cliente es: {data.decode()}")
                if not data:
                    break
                conection.sendall(data)

start_server()
