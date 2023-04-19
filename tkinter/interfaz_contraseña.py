import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Generador de contraseñas")

        self.length_label = tk.Label(master, text="Longitud:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()
        self.length_entry.insert(0, "8")

        self.include_uppercase_var = tk.IntVar()
        self.include_uppercase_checkbutton = tk.Checkbutton(master, text="Incluir mayúsculas", variable=self.include_uppercase_var)
        self.include_uppercase_checkbutton.pack()

        self.include_special_var = tk.IntVar()
        self.include_special_checkbutton = tk.Checkbutton(master, text="Incluir caracteres especiales", variable=self.include_special_var)
        self.include_special_checkbutton.pack()

        self.generate_button = tk.Button(master, text="Generar contraseña", command=self.generate_password)
        self.generate_button.pack()

        self.strength_button = tk.Button(master, text="Comprobar fortaleza", command=self.check_strength)
        self.strength_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        include_uppercase = bool(self.include_uppercase_var.get())
        include_special = bool(self.include_special_var.get())

        letters = string.ascii_lowercase
        if include_uppercase:
            letters += string.ascii_uppercase
        if include_special:
            letters += string.punctuation

        password = ''.join(random.choice(letters) for _ in range(length))

        self.password_label.config(text=password)

