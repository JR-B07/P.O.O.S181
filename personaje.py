class Personaje:
    #atributos
    especie= "Humano"
    nombre= "Augustus Cole"
    altura= 1.87
    
    #METODOS PERSONAJE
    
    def correr(self,status):
        if(status):
            print("EL personaje "+ self.nombre + "esta corriendo")
        else:
            print("EL personaje " + self.nombre + "se detuvo" )
            
    def lanzarGranada(self):
        print("se lanzo granada ")
        
    def recargarArma(self,municiones):
        cargador= 5
        cargador = cargador + municiones
        print("El arma tiene ahora " + cargador + "balas")
        