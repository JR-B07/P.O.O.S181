class Personaje:
    #Creamos el constructor
    def __init__(self, esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #METODOS PERSONAJE
    
    def correr(self,status):
        if(status):
            print("EL personaje "+ self.__nombre + "esta corriendo")
        else:
            print("EL personaje " + self.__nombre + "se detuvo" )
            
    def lanzarGranada(self):
        print("se lanzo granada ")
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador = cargador + municiones
        print("El arma tiene ahora" + str(cargador) + "balas")
    
    #Ejemplo del método Privado
    def __pensar(self):
         print("pa pensarse.........")
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self._especie= esp
        
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nom):
        self._nombre= nom
    
    def getaltura(self):
        return self.__altura
    
    def setaltura(self,alt):
        self.__altura= alt
