#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',1234)
server_socket.bind(server_address)

server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    print(f"\n [+] Mensaje recibido del cliente: {data.decode()}")
    print(f"\n [+] Informacion del cliente que se ha comunicado con nosotros: {client_address}")

    client_socket.sendall(f"\n [I] Un saludo crack [I]".encode())
    client_socket.close()
