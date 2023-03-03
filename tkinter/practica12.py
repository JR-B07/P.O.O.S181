import tkinter as tk

class LoginWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.email_label = tk.Label(self.master, text="Correo electrónico:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5)

        self.password_label = tk.Label(self.master, text="Contraseña:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        # Entries
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.login_button = tk.Button(self.master, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=2, column=0, padx=5, pady=5)

        self.quit_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.quit_button.grid(row=2, column=1, padx=5, pady=5)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(master=root)
    app.mainloop()
