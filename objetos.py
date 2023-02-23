
#1importar clases
from personaje import*

#2Solicitar atributos para el objeto
print("")
print("### Solicitud de datos del Heroe ###")
espH= input("Escribe la especie del Heroe")
nomH= input("Escribe el nombre del Heroe")
altH= float(input("Escribe la altura del Heroe"))
cargaH= int(input("Cuantas balas se recargan al Heroe"))

print("")
print("### Solicitud de datos del Villano ###")
espV= input("Escribe la especie del Villano")
nomV= input("Escribe el nombre del Villano")
altV= float(input("Escribe la altura del Villano"))
cargaV= int(input("Cuantas balas se recargan al Villano"))

#3 Creamos 2 objetos 
Heroe= Personaje(espH,nomH,altH)
Villano= Personaje(espV,nomV,altV)

#.Instanciar un objeto 
#Heroe= Personaje()

#4acceder a sus atributos
print("")
print("## Atributos personaje ##")
print("El personaje pertenece a la raza: " + Heroe.especie)
print("Se llama : " + Heroe.nombre)
print("mide : " + str(Heroe.altura) + "Metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

print("")
print("## Atributos personaje ##")
print("El personaje pertenece a la raza: " + Villano.especie)
print("Se llama : " + Villano.nombre)
print("mide : " + str(Villano.altura) + "Metros")
print("")

Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)