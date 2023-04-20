from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controlador import controlador


ventana = Tk()
ventana.title("BD EXPORTACIONES")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)

# Creamos un objeto de la clase controlador
controlador = controlador()

# Función para disparar el botón
def ejecutaInsert():
    controlador.insertarExpo(varId.get(),varTrans.get(),varAdua.get())

def ejecutaBorrar():
    idUsuario = varIdElim.get()
    confirmacion = messagebox.askyesno("Confirmación")
    if confirmacion:
        controlador.elim(IdExpo)
        messagebox.showinfo("Eliminación exitosa")
    else:
        messagebox.showinfo("Eliminación cancelada")

#Pestaña 1: REGISTRO 

titulo1 = Label(pestaña1,text="REGISTRO", fg='green', font=("Modern",18)).pack()

varId = StringVar()
Label(pestaña1, text="IDEXPO ").pack()
Entry(pestaña1, textvariable=varId).pack()

varTrans = StringVar()
Label(pestaña1, text="Transporte ").pack()
Entry(pestaña1, textvariable=varTrans).pack()

varAdua = StringVar()
Label(pestaña1, text="Aduana").pack()
Entry(pestaña1, textvariable=varAdua, show="*").pack()

btnGuardar = Button(pestaña1, text="Guardar Información", command=ejecutaInsert)
btnGuardar.pack()

#Pestaña 2: Eliminar Registro

titulo5 = Label(pestaña2,text="Eliminar Registro", fg='blue', font=("Modern",18)).pack()

varIdElim = StringVar()
Label(pestaña2, text="IDExpo: ").pack()
Entry(pestaña2, textvariable=varIdElim).pack()

btnEliminar = Button(pestaña2, text="Eliminar Registro", command=ejecutaBorrar)
btnEliminar.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')

ventana.mainloop()