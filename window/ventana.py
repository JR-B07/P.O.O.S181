
from tkinter import *
from tkinter import messagebox
from Usuario import Usuario1 

class VentanaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        
        self.lbl_correo = Label(self.master, text="Correo electrónico:")
        self.lbl_correo.pack()
        self.ent_correo =Entry(self.master)
        self.ent_correo.pack()
        
        self.lbl_contrasena =Label(self.master, text="Contraseña:")
        self.lbl_contrasena.pack()
        self.ent_contrasena =Entry(self.master, show="*")
        self.ent_contrasena.pack()
        
        self.btn_ingresar =Button(self.master, text="Ingresar", command=self.verificar_credenciales)
        self.btn_ingresar.pack()
    
    def verificar_credenciales(self):
        correo = self.ent_correo.get()
        contrasena = self.ent_contrasena.get()
        
        if correo == "" or contrasena == "":
            messagebox.showerror("Error", "Debe ingresar correo y contraseña")
            return
        
        Usuario = Usuario1("correo@example.com", "contrasena")
        
        if Usuario.verificar_credenciales(correo, contrasena):
            messagebox.showinfo("Bienvenido", "Bienvenido al sistema")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Por favor, revise sus datos.")
