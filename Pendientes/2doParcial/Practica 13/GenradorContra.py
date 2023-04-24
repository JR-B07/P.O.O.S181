import string
import random
import tkinter as tk
from tkinter import messagebox


class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Generador de contraseñas")

        self.length_label = tk.Label(master, text="Longitud:")
        self.length_label.grid(row=0, column=0, sticky="w")

        self.length_entry = tk.Entry(master)
        self.length_entry.insert(0, "8")
        self.length_entry.grid(row=0, column=1, sticky="w")

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(master, text="Incluir mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbutton.grid(row=1, column=0, sticky="w")

        self.special_var = tk.BooleanVar()
        self.special_checkbutton = tk.Checkbutton(master, text="Incluir caracteres especiales", variable=self.special_var)
        self.special_checkbutton.grid(row=2, column=0, sticky="w")

        self.strength_button = tk.Button(master, text="Comprobar fortaleza", command=self.check_strength)
        self.strength_button.grid(row=3, column=0, sticky="w")

        self.generate_button = tk.Button(master, text="Generar contraseña", command=self.generate_password)
        self.generate_button.grid(row=3, column=1, sticky="w")

        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=4, column=0, columnspan=2)



root = tk.Tk()
gui = PasswordGenerator(root)
root.mainloop()
