#!/usr/bin/env python3

import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def client_thread(client_socket, clients, usernames):
    print(f"\n[+] Estamos en la parte del client_thread")

    username = client_socket.recv(1024).decode().strip()
    usernames[client_socket] = username

    for client in clients:
        if client is not client_socket:
            try:
                client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode())
            except BrokenPipeError:
                clients.remove(client)
                client.close()

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message.strip().startswith("[-] El usuario") and "se ha desconectado" in message:
                print("Entrada al mensaje de desconexion")

                for client in clients:
                    if client is not client_socket:
                        try:
                            client.sendall(message.encode())
                        except:
                            clients.remove(client)
                            client.close()

                if client_socket in clients:
                    clients.remove(client_socket)
                if client_socket in usernames:
                    del usernames[client_socket]
                break

            if message == "!usuarios":
                print("Entrada al listado de usuarios disponibles")
                client_socket.sendall(
                    f"\n[+] Listado de usuarios disponibles: {', '.join(usernames.values())}\n\n".encode()
                )
                continue

            for client in clients:
                if client is not client_socket:
                    try:
                        client.sendall(message.encode())
                    except:
                        clients.remove(client)
                        client.close()

        except:
            break


    if client_socket in clients:
        clients.remove(client_socket)
    if client_socket in usernames:
        del usernames[client_socket]
    client_socket.close()
    print(f"[-] {username} eliminado de la lista. Usuarios actuales: {list(usernames.values())}")


def server_programing():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"\n[+] El servidor está en escucha de conexiones entrantes...")

    clients = []
    usernames = {}

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"\n[+] Se ha conectado un nuevo cliente: {client_address}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    server_programing()
