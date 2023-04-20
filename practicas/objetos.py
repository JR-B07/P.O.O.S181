
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

#Ejemplo del uso del Set
Heroe.setnombre("GDR15")
#.Instanciar un objeto 
#Heroe= Personaje()

#4acceder a sus atributos
print("")
print("## Atributos personaje ##")
print("El personaje pertenece a la raza: " + Heroe.getEspecie())
print("Se llama : " + Heroe.getnombre())
print("mide : " + str(Heroe.getaltura()) + "Metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

print("")
print("## Atributos personaje ##")
print("El personaje pertenece a la raza: " + Villano.getEspecie())
print("Se llama : " + Villano.getnombre())
print("mide : " + str(Villano.getaltura()) + "Metros")
print("")

Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)