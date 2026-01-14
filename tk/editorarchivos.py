#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:

    def __init__(self, ventana):
        self.ventana = ventana
        self.text_area = tk.Text(self.ventana)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ''

    def salir(self):
        if messagebox.askokcancel("Salir", "Estas seguro que quieres salir del programa?"):
            print("Saliendo")
            self.ventana.destroy()

    def save_file(self):
        if not self.current_open_file:
            file = filedialog.asksaveasfilename()

            if file:
                self.current_open_file = file
            else:
                return
        with open(file, 'w') as f:
            f.write(self.text_area.get("1.0", tk.END))

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file = ''

    def open_file(self):
        filename = filedialog.askopenfilename()

        if filename:
            self.text_area.delete("1.0", tk.END)
            with open(filename, 'r') as f:
                self.text_area.insert("1.0", f.read())
        self.current_open_file = filename

ventana = tk.Tk()

editor = SimpleTextEditor(ventana)

menu_bar= tk.Menu(ventana)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.salir)

ventana.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)


ventana.mainloop()
