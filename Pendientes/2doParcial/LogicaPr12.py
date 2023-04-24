from tkinter import *
import tkinter as tk
from Pract12 import *

Login = Log()

def ejecutaLogin():
    Login.validarDatos(correo.get(), contraseña.get())

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x400")

section0= Frame(ventana)
section0.pack(expand=True, fill= "both")

titulo= Label(section0,text="LOGIN SISTEM", bg="black", fg="white", font=("Algerian", 22)).pack

correo= tk.StringVar()
correo_label = tk.Label(section0, text="Correo:").pack()
correo_entry = tk.Entry(section0, textvariable=correo, takefocus=True).pack()

contraseña= tk.StringVar()
contrasena_label = tk.Label(section0, text="Contraseña:").pack()
contrasena_entry = tk.Entry(section0, show="*", textvariable=contraseña).pack()

boton_login = tk.Button(section0, text="Login", bg="blue", command=ejecutaLogin)
boton_login.pack()

ventana.mainloop()
