#Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
#Solicitando al usuario la cantidad de * de la base

base = int(input("Introduce la cantidad de asteriscos en la base del árbol: "))

altura = base // 2 + 1
espacios = altura - 1
asteriscos = 1

while altura > 0:
    for i in range(espacios):
        print(" ", end="")
    
    for i in range(asteriscos):
        print("*", end="")
    print()
    
    altura -= 1
    espacios -= 1
    asteriscos += 2

tronco_altura = base // 4
tronco_espacios = base // 2 - tronco_altura // 2

while tronco_altura > 0:
    for i in range(tronco_espacios):
        print(" ", end="")
    
    for i in range(tronco_altura):
        print("*", end="")
    print()
    
    tronco_altura -= 1

