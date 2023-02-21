
#importar clases
from personaje import*

#2.Instanciar un objeto 
Heroe= Personaje()

#acceder a sus atributos
print("Atributos personaje")
print("El personaje pertenece a la raza: " + Heroe.especie)
print("Se llama : " + Heroe.nombre)
print("mide : " + str(Heroe.altura) + "Metros")
print("METODOS DEL PERSONAJE")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)