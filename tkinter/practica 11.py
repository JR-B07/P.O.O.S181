from tkinter import Tk,Frame,Button,messagebox
def mostrarMensaje():
    messagebox.showinfo("Aviso", "Este mensaje es para informar algo ")
    messagebox.showerror("Este es un mensaje de error:" "todo fallo con exito")
    print(messagebox.ask("Pregunta:", "EL o ella jugo con tu corazón "))
#Funcion para agregar botones
def agregarBoton():
        botonNegro.config(text="+",bg="green", fg="white")
        botonNuevo= Button(seccion3,text="Boton Nuevo")
        botonNuevo.pack()
#!. Instanciamos un objeto Ventana 
ventana= Tk()
ventana.title("Practica 11: Frames")
ventana.geometry("600x400")

#2.DEFINIMOS SECCIONES A LA VENTANA
seccion1=Frame(ventana,bg= "red")
seccion1.pack(expand=True,fill="both") 

seccion2=Frame(ventana, bg="#0088cc")
seccion2.pack(expand=True,fill="both")

seccion3=Frame(ventana, bg="#2a8000")
seccion3.pack(expand=True,fill="both")

#3 
botonAzul= Button(seccion1, text="boton gris", fg="blue", command= mostrarMensaje)
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2, text="boton amarillo", fg="gray")
botonAmarillo.grid(row=0, column=0)

botonRojo= Button(seccion2, text="boton negro", bg="black", fg='white')
botonRojo.grid(row=0, column=1)

botonNegro= Button(seccion3, text="boton negro", bg="#ff1aff", command=agregarBoton)
botonNegro.pack()

#Debe ir al final del codigo para que se ejecute
ventana.mainloop()