import tkinter as tk
from tkinter import messagebox
from LogicaCon import *

def convert():
    if var.get() == 'romano a arabigo':
        if not validar_romano_numeral(entry.get()):
            messagebox.showerror("Numero Invalido")
        else:
            arabigo_numeral = romano_a_arabigo_convert(entry.get())
            messagebox.showinfo("Result", f"El Numero Arabigo es: {arabigo_numeral}")
    elif var.get() == 'arabigo a romano':
        if not validar_number(entry.get()):
            messagebox.showerror("Numero Invalido")
        else:
            romano_numeral = arabigo_a_romano_convert(int(entry.get()))
            messagebox.showinfo("Resultado", f"El Numero Romano es: {romano_numeral}")


window = tk.Tk()
window.title("Convertidor de Num. Romanos y Arabigos")


label = tk.Label(window, text="Ingresa un Número Arabigo o Romano del (1-50):")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)


var = tk.StringVar(value='romano a arabigo')
option1 = tk.Radiobutton(window, text='romano a arabigo', variable=var, value='romano a arabigo')
option1.pack()
option2 = tk.Radiobutton(window, text='arabigo a romano', variable=var, value='arabigo a romano')
option2.pack()

convert_button = tk.Button(window, text='Convert', command=convert)
convert_button.pack(pady=10)

window.mainloop()