#!/usr/bin/env python3

import socket

def start_udp_server():
    host = '127.0.0.1'
    port = 1235

    #UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\n [+] Servidor UDP iniciando en {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n [+] Mensaje del cliente: {data.decode()}")
            print(f"\n [!] Informacion del cliente: {addr} ")

start_udp_server()
