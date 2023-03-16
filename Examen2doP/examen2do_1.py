import random
import datetime
import tkinter as tk

# Función para generar la matrícula 
def generar_matricula():
    # Obteniendo los datos del usuario
    nombre = nombre_entry.get()
    apellido_paterno = apellido_paterno_entry.get()
    apellido_materno = apellido_materno_entry.get()
    anio_nacimiento = anio_nacimiento_entry.get()
    carrera = carrera_entry.get()
    
    # Obteniendo los digitos del año actual y de nacimiento
    anio_actual = datetime.datetime.now().year % 100 # Obteniendo los ultimos dos digitos del año actual
    anio_nacimiento = str(anio_nacimiento)[-2:] # Obteniendo los dos ultimos digitos de nacimiento
    
    # Obteniendo las letras iniciales 
    letra_nombre = nombre[0]
    letra_apellido_paterno = apellido_paterno[:2]  
    letra_apellido_materno = apellido_materno[:2]
    
    # Digitos
    digitos_aleatorios = '{:02d}'.format(random.randit(0, 99))
    
    #obteniendo 
    
    
    
    