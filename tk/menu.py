#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, filedialog

root= tk.Tk()
root.title("Menu() Widget")

def poner_mensaje():
    messagebox.showinfo("Menu", "Se ha tensado la thing")


def mostrar_ruta():
    ruta_archivo= filedialog.askopenfilename()
    label_ruta.config(text=ruta_archivo)


#Label ruta
label_ruta = tk.Label(root, text="")
label_ruta.pack()


#barra prinicpal del menu
barra_menu= tk.Menu(root)
root.config(menu=barra_menu)

#primer opcion del menu
menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu", menu=menu1)

menu1.add_command(label="Opc1", command=mostrar_ruta)
menu1.add_command(label="Opc2")

#segunda opcion del menu
menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)

menu2.add_command(label="Se tensa", command=poner_mensaje)

root.mainloop()
