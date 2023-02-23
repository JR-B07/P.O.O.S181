class Personaje:
    #Creamos el constructor
    def __init__(self, esp,nom,alt):
     self.especie= esp
     self.nombre= nom
     self.altura= alt
    
    #METODOS PERSONAJE
    
    def correr(self,status):
        if(status):
            print("EL personaje "+ self.nombre + "esta corriendo")
        else:
            print("EL personaje " + self.nombre + "se detuvo" )
            
    def lanzarGranada(self):
        print("se lanzo granada ")
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador = cargador + municiones
        print("El arma tiene ahora" + str(cargador) + "balas")
        