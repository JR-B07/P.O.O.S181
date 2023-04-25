#Programa Conversor de Unidades

def mb_a_gb(mb):
    gb = mb / 1024
    return gb

def gb_a_mb(gb):
    mb = gb * 1024
    return mb

def gb_a_tb(gb):
    tb = gb / 1024
    return tb

def tb_a_gb(tb):
    gb = tb * 1024
    return gb

valor = float(input("Ingrese el valor a convertir: "))
U_base = input("Ingrese la unidad base (MB, GB, TB): ")
U_a_conver = input("Ingrese la unidad a convertir (MB, GB, TB): ")
if U_base == "MB":
    if U_a_conver == "GB":
        resultado = mb_a_gb(valor)
        print(f"{valor} MB equivale a {resultado} GB")
    else:
        print("No se puede realizar la conversión")

elif U_base == "GB":
    if U_a_conver == "MB":
        resultado = gb_a_mb(valor)
        print(f"{valor} GB equivale a {resultado} MB")
    elif U_a_conver == "TB":
        resultado = gb_a_tb(valor)
        print(f"{valor} GB equivale a {resultado} TB")
    else:
        print("No se puede realizar la conversión")
        
elif U_base == "TB":
    if U_a_conver == "GB":
        resultado = tb_a_gb(valor)
        print(f"{valor} TB equivale a {resultado} GB")
    else:
        print("No se puede realizar la conversión")
else:
    print("La unidad base ingresada no es válida")