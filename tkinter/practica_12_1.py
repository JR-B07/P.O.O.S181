import tkinter as tk

class Usuario(tk):
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            self.display_message("Por favor ingrese correo y contraseña.")
        elif email == "jrbc@gmail.com" and password == "1234":
            self.display_message("¡Bienvenido!")
        else:
            self.display_message("Usuario o contraseña incorrectos.")

    def display_message(self, message):
        self.message_label = tk.Label(self.master, text=message)
        self.message_label.grid(row=3, columnspan=2, padx=5, pady=5)
