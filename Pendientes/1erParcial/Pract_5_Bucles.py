#un programa que pida al usuario un número entero positivo y muestre
#por pantalla todos los números impares desde 1 hasta ese número separados
#por comas.

numero = int(input("Ingresa un número entero positivo: "))
impares = []

for i in range(1, numero + 1):
    if i % 2 != 0:
        impares.append(i)

print("Los números impares hasta el número ingresado son:", end=" ")
for impar in impares:
    print(impar, end=", ")
    
    
