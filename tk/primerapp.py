#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

def salir():
    print(f"\n[!] Saliending...")
    ventana.destroy()

def accion_de_boton():
    print(f"\n[+] Se ha presionado el boton")

def get_data():
    data = entry_widget.get("1.0", tk.END).strip()
    mensaje = ""
    if data:
        mensaje = f"Hola, {data}"
    else:
        messagebox.showinfo("Menu", "Escribe un mensaje en la caja")
    label_salida_datos.config(text=mensaje)

#Ventana
ventana = tk.Tk()

#Frame Superior
frame_top = tk.Frame(ventana, bg="lightgray", height=10)
frame_top.pack(fill="both", expand=True)
#Label Principal
label = tk.Label(ventana, text="Mi primera aplicacion", bg="blue")
label.pack(side="top",fill=tk.X)
#Boton Principal (1)
boton = tk.Button(ventana, text="Pulsame", command=accion_de_boton)
boton.pack(pady=15)
#Entrada de datos
entry_widget = tk.Text(ventana)
entry_widget.pack(pady=5, padx=15, fill=tk.X)
#Boton para entrada de datos
boton_entrada = tk.Button(ventana, text="Recoger datos",command=get_data)
boton_entrada.pack(fill=tk.X)
#label salida
label_salida_datos=tk.Label(ventana, text="")
label_salida_datos.pack(fill=tk.X)
#Zona Inferior
frame_botom = tk.Frame(ventana, bg="lightgray", height=100)
frame_botom.pack(fill="both", expand=True)
#Boton Inferior
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(side="bottom",pady=10)

ventana.mainloop()

