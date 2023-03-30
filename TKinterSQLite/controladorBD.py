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
        conH= self.encriptarCon(con)
        datos=(nom,cor,con)
        qrInsert= "insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
        
        #4 Ejecutar Insert y cerramos Conexión
        cursor.execute(qrInsert,datos)
        conx.commit()
        conx.close
        messagebox.showinfo("Exito","Usuario Guardado")
        
#Metodo para encryptar contraseñas
    def encriptarCon(self, con):
        conPlana= con
        
        #metodo para encriptar contraseñas
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt() #gensalt es algoritmo de aleatoriedad
        conHA= bcrypt.hashpw(conPlana,sal)  #hashpw te da la contraseña encriptada
        print(conHA)
        #enviamos la contraseña encriptada
        return conHA 
    
    # metodo para buscar 1 usuario
    
    def consultarUsuario(self,id):
        #preparar una conexción
        conx= self.conexionBD()
        
        #2. verificar si id contiene algo
        if(id == ""):
            messagebox.showwarning("cuidado", "Id vacio escribe algo valido")
        else:
            try:
                #3. preparar consulta y el query
                cursor= conx.cursor()
                selectQry= "select * from TBRegistrados where id= "+id
                
                #4. ejecutar y guardar la consulta 
                cursor.execute(selectQry)
                rsUsuario= cursor.fetchall()
                conx.close()
                
                return rsUsuario
            
            except sqlite3.OperationalError:
                print("Error Consulta ")
        