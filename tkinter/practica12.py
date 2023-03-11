import tkinter as tk
import practica_12_1

instancia = practica_12_1.Usuario()
class ventanainicio(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.create_widgets()

    def create_widgets(self):
     # datos
        self.email_label = tk.Label(self.master, text="Correo electrónico:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5)

        self.password_label = tk.Label(self.master, text="Contraseña:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        # Entradas de txt
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones
        self.login_button = tk.Button(self.master, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=2, column=0, padx=5, pady=5)

        self.quit_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.quit_button.grid(row=2, column=1, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ventanainicio(master=root)
    app.mainloop()
