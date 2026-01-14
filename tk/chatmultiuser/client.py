#!/usr/bin/env python3

import socket
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading

def send_message(event, client_socket, username, text_widget, entry_widget):
    data = entry_widget.get()
    if not data.strip():
        return
    client_socket.sendall(f"{username} > {data}\n".encode())

    entry_widget.delete(0, END)
    text_widget.config(state="normal")
    text_widget.insert(END, f"{username}: {data}\n")
    text_widget.config(state="disabled")

def recive_message(client_socket, text_widget):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            text_widget.config(state="normal")
            text_widget.insert(END, data + "\n")
            text_widget.config(state="disabled")
            text_widget.see("end")
        except:
            break

def list_users_request(client_socket):
    client_socket.sendall("!usuarios".encode())

def salir(window, username, client_socket, text_widget):
    try:
        client_socket.sendall(f"[-] El usuario {username} se ha desconectado del chat".encode())
    except:
        pass
    window.destroy()
    print("saliendo...")

def client_program():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    username = input(f"\n[+] Introduce tu usuario: ")
    client_socket.sendall(username.encode())

    window = Tk()
    window.title("Chat")

    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=2, fill=BOTH, expand=1)

    text_widget = ScrolledText(window, state='disabled')
    text_widget.pack(padx=10, pady=10, fill=BOTH)

    entry_widget = Entry(window)
    entry_widget.bind("<Return>", lambda event: send_message(event, client_socket, username, text_widget, entry_widget))
    entry_widget.pack(pady=5, fill=BOTH, padx=5)

    b_salir = Button(frame_widget, text="Salir", command=lambda: salir(window, username, client_socket, text_widget))
    b_salir.pack(side=LEFT, padx=5, pady=5)

    users_widget = Button(frame_widget, text="Listar usuarios", command=lambda: list_users_request(client_socket))
    users_widget.pack(side=LEFT, padx=5, pady=5)

    thread = threading.Thread(target=recive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    window.protocol("WM_DELETE_WINDOW", lambda: salir(window, username, client_socket, text_widget))
    window.mainloop()

    try:
        client_socket.close()
    except:
        pass

if __name__ == '__main__':
    client_program()
