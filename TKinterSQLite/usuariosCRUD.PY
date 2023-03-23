from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana= Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel= ttk.Notebook(ventana)
panel.pack(fill="both" ,expand="yes")

pestaña1= ttk.Frame(panel)
pestaña2= ttk.Frame(panel)
pestaña3= ttk.Frame(panel)
pestaña4= ttk.Frame(panel)

#PESTAÑA 1 FORMULARIO DE U

titulo= Label(pestaña1,text="Registro de usuarios", fg="blue",front=("modern", 18)).pack

varNom= tk.StringVar()
IblNom= Label(pestaña1,text= "Nombre: ").pack()
txtNom= Entry(pestaña1,textvariable=varNom).pack()

varCor= tk.StringVar()
IBlCor= Label(pestaña1, text="Correo: ").pack()
txtCor= Entry(pestaña1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestaña1,text= "Nombre: ").pack()
txtCoN= Entry(pestaña1,textvariable=varCon).pack()

btnGuardar= Button(pestaña1, text= "contraseña: ").pack()


panel.add(pestaña1, text="Formulario de usuarios")
panel.add(pestaña2, text="Buscar usuario")
panel.add(pestaña3, text="Consultar de usuario")
panel.add(pestaña4, text="Actualizar usuario")

ventana.mainloop()
