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

    # Obteniendo los dígitos del año actual y de nacimiento
    anio_actual = datetime.datetime.now().year % 100  # Obteniendo los últimos dos dígitos del año actual
    anio_nacimiento = str(anio_nacimiento)[-2:]  # Obteniendo los últimos dos dígitos del año de nacimiento

    # Obteniendo las letras iniciales
    letra_nombre = nombre[0]
    letra_apellido_paterno = apellido_paterno[:2]
    letra_apellido_materno = apellido_materno[:2]

    # Generando los dígitos aleatorios
    digitos_aleatorios = '{:02d}'.format(random.randint(0, 99))

    # Obteniendo las primeras tres letras de la carrera
    letras_carrera = carrera[:3]

    # Concatenando los elementos para formar la matrícula
    matricula = f"{letra_nombre}{letra_apellido_paterno}{letra_apellido_materno}{anio_nacimiento}{anio_actual}{letras_carrera}{digitos_aleatorios}"
    # Mostrando la matrícula generada
    matricula_label.config(text=f"Tu matrícula es: {matricula}")

# Creando la ventana de la aplicación
app = tk.Tk()
app.title("Generador de matrículas")

# Creando los campos de entrada para los datos del usuario
nombre_label = tk.Label(app, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(app)
nombre_entry.pack()

apellido_paterno_label = tk.Label(app, text="Apellido paterno:")
apellido_paterno_label.pack()
apellido_paterno_entry = tk.Entry(app)
apellido_paterno_entry.pack()

apellido_materno_label = tk.Label(app, text="Apellido materno:")
apellido_materno_label.pack()
apellido_materno_entry = tk.Entry(app)
apellido_materno_entry.pack()

anio_nacimiento_label = tk.Label(app, text="Año de nacimiento:")
anio_nacimiento_label.pack()
anio_nacimiento_entry = tk.Entry(app)
anio_nacimiento_entry.pack()

carrera_label = tk.Label(app, text="Carrera:")
carrera_label.pack()
carrera_entry = tk.Entry(app)
carrera_entry.pack()

# Creando el botón para generar la matrícula
generar_matricula_button = tk.Button(app, text="Generar matrícula", command=generar_matricula)
generar_matricula_button.pack()

# Creando la etiqueta para mostrar la matrícula generada
matricula_label = tk.Label(app, text="")
matricula_label.pack()

# Iniciando el loop principal de la aplicación
app.mainloop()