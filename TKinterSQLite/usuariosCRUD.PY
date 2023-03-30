from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import controladorBD
from controladorBD import guardarUsuario
#1 presentamos los archivo controlador vista

#2 cremos 1 objeto de la clase controlador
controlador= controladorBD()

#3.Funcion para disparar el boton
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#4 Funcion para disparar el botom de busqueda
def ejecutarSelect():
    controlador.consultarUsuario(varBus.get())

    for usu in Usuario:
        cadena= str(usu{0})+ " " + usu{1} + " " usu{2} + " "+ str(usu{3})
        
    if(usu):
        print(cadena)
    else:
        messagebox.showinfo("No encontrado", "El usuario no existe en la BD")
         
ventana= Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel= ttk.Notebook(ventana)
panel.pack(fill="both" ,expand="yes")

pestaña1= ttk.Frame(panel)
pestaña2= ttk.Frame(panel)
pestaña3= ttk.Frame(panel)
pestaña4= ttk.Frame(panel)

#PESTAÑA 1 FORMULARIO DE Usuario
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

btnGuardar= Button(pestaña1, text= "Guardar usuario",command=ejecutaInsert).pack()


#PESTAÑA 2: BUSQUEDA DE USUARIO

titulo2= Label(pestaña2,text="Busqueda de usuarios", fg="green",front=("Modern", 18)).pack

varBus= tk.StringVar()
Iblid= Label(pestaña2,text= "Identificador de usuario: ").pack()
txtid= Entry(pestaña2,textvariable=varBus).pack()
btnBus= Button(pestaña2, text= "Buscar usuario",command=ejecutaInsert).pack()

subBus= Label(pestaña2,text="Encontrado", fg="red",front=("Modern", 15)).pack
textEnc= tk.Text(pestaña2,height=5,width=52).pack()

panel.add(pestaña1, text="Formulario de usuarios")
panel.add(pestaña2, text="Buscar usuario")
panel.add(pestaña3, text="Consultar de usuario")
panel.add(pestaña4, text="Actualizar usuario")

ventana.mainloop()