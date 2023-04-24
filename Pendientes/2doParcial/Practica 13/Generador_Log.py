from tkinter import *
from tkinter import messagebox
from GenradorContra import PasswordGenerator

def generate_password(self):
        length = int(self.length_entry.get())
        chars = str.ascii_lowercase
        if self.uppercase_var.get():
            chars += str.ascii_uppercase
        if self.special_var.get():
            chars += str.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        self.password_label.configure(text=password)

def check_strength(self):
        password = self.password_label.cget("text")
        if len(password) < 8:
            messagebox.showinfo("Fortaleza de contraseña", "La contraseña es débil")
        elif any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            messagebox.showinfo("Fortaleza de contraseña", "La contraseña es fuerte")
        else:
            messagebox.showinfo("Fortaleza de contraseña", "La contraseña es media")