from tkinter import messagebox
import sqlite3
import tkinter
from typing import Self
import bcrypt

class controlador:
    
    def __init__(self):
        pass
   
    def conexionBD(self):
     
     try:
        conexion = sqlite3.connect("C:/Users/india/Documents/POO/GitHub/S181/Examen3erP/BDExportaciones.db")
        print("Conectado a la Base de Datos")
        return conexion
     except sqlite3.OperationalError:
        print("No se puede conectar")
    
#Metodo para guardar Registros
    def guardarExpo(self,Id,Trans,Adua):
        # paso 1: usamos una conexion
        conx = self.conexionBD()
        # paso 2: validar parametros que esten vacios
        if(Id=="" or Trans=="" or Adua ==""):
         messagebox.showwarning("Formulario Incompleto")
        else:
        # paso 3: preparamos el cursor, datos y QuerySQL
         cursor = conx.cursor()
         datos = (Id,Trans,Adua)
         qrInsert = "insert into BDExportaciones(nombre,correo,contraseña) values(?,?,?)"
        # paso 4: ejecutar Insert y cerramos conexion
         cursor.execute(qrInsert,datos)
         conx.commit()
         conx.close
        messagebox.showinfo("Exito","Registro Guardado")
        
    def elimExpo(self, Id):
            # 1. Preparar una conexión
            cons = self.conexionBD()
            # 2. Verificar si el ID está vacío
            if(Id == ""):
                messagebox.showwarning("ID vacío")
                cons.close()
            else:
                try:
                    # 3. Preparar cursor y query
                    cursor = cons.cursor()
                    # 4. Eliminar el registro
                    elimQuery = f"Borrar FROM TBRegistrados WHERE id={Id}"
                    cursor.execute(elimQuery)
                    # 5. Guardar los cambios y cerrar la conexión
                    cons.commit()
                    cons.close()
                    messagebox.showinfo("Exito", "Registro eliminado")
                except sqlite3.OperationalError:
                    print("Error eliminando usuario")