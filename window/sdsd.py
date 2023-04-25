import tkinter as tk
from tkinter import messagebox

# Función para convertir números romanos a arábigos
def roman_to_arabic(roman_num):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    arabic_num = 0
    prev_value = 0
    for i in reversed(roman_num):
        value = roman_dict[i]
        if value < prev_value:
            arabic_num -= value
        else:
            arabic_num += value
        prev_value = value
    return arabic_num

# Función para convertir números arábigos a romanos
def arabic_to_roman(arabic_num):
    arabic_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}
    roman_num = ''
    for key in reversed(sorted(arabic_dict)):
        while arabic_num >= key:
            roman_num += arabic_dict[key]
            arabic_num -= key
    return roman_num

# Función para convertir el número
def convert_num():
    num = entry_num.get()
    if num.isnumeric():
        num = int(num)
        if 1 <= num <= 50:
            if var.get() == 1:
                messagebox.showinfo("Resultado", f"{num} en números arábigos es: {arabic_to_roman(num)}")
            else:
                messagebox.showinfo("Resultado", f"{num} en números romanos es: {roman_to_arabic(entry_num.get().upper())}")
        else:
            messagebox.showwarning("Advertencia", "El número debe estar entre 1 y 50")
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un número válido")

# Crear la ventana
window = tk.Tk()
window.title("Conversor de números romanos y arábigos")
window.geometry("400x200")

# Crear la etiqueta para el número
label_num = tk.Label(window, text="Número:")
label_num.pack()

# Crear la entrada para el número
entry_num = tk.Entry(window)
entry_num.pack()

# Crear los botones de conversión
var = tk.IntVar()
var.set(1)
button_roman_to_arabic = tk.Radiobutton(window, text="Romano a Arábigo", variable=var, value=1)
button_arabic_to_roman = tk.Radiobutton(window, text="Arábigo a Romano", variable=var, value=2)
button_roman_to_arabic.pack()
button_arabic_to_roman.pack()

# Crear el botón de conversión
button_convert = tk.Button(window, text="Convertir", command=convert_num)
button_convert.pack()

# Ejecutar la ventana
window.mainloop()
