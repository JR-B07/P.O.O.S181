from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/india/Documents/GitHub/S181/TKinterSQLite/TBRegistrados.db")
            print("Concectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")

#Metodos para Guardar Usuarios   
def guardarUsuario(self,nom,cor,con):
    
    #1 usamos una conexión
    conx= self.conexionBD()
    
    #2 validar parametros vacios
    if(nom == "" or cor == "" or con == "" ):
        messagebox.showwarning("Aguas", "Formulario Incompleto")
    else:
        
        # 3 preparamos cursor,datos,querysql
        cursor= conx.cursor()
        datos=(nom,cor,con)
        qrInsert= "insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
        
        #4 Ejecutar Insert y cerramos Conexión
        cursor.execute(qrInsert,datos)
        conx.commit()
        conx.close
        messagebox.showinfo("Exito","Usuario Guardado")
        