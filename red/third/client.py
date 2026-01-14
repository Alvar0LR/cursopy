#!/usr/bin/env python3

import socket

def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
        socket_client.connect((host, port))

        while True:
            message = input(f"\n [+] Introduce tu mensaje: ")
            socket_client.sendall(message.encode())

            if message == 'bye':
                break

            data = socket_client.recv(1024)
            print(f"\n [+] La respuesta del servidor es: {data.decode()}")

start_client()

