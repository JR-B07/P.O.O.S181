from tkinter import messagebox

class Log:
    
    def __init__(self):
        self.__correo1= "R01.becerra@gmail.com"
        self.__contraseña1= "12345"
        
    def validarDatos(self,correo,contraseña):
        
        if (correo == "" or contraseña == ""):
              messagebox.showwarning("Completa los campos")
        else:
            if (self.__correo1 == correo and self.__contraseña1 == contraseña):
             messagebox.showinfo("Bienvenido nuevamente")
            else:
                messagebox.showerror("Datos incorrectos")