class Usuario1:
    def __init__(self, correo, contrasena):
        self.correo = correo
        self.contrasena = contrasena
    
    def verificar_credenciales(self, correo, contrasena):
        if correo == self.correo and contrasena == self.contrasena:
            return True
        else:
            return False


