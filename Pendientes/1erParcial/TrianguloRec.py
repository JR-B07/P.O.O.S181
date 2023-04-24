#un programa que pida al usuario un número entero y muestre por
#pantalla un triángulo rectángulo como el de más abajo, de altura el número
#introducido.

num = int(input("Introduce un número entero: "))

for i in range(1, num+1):
    # Imprime los números impares de 1 hasta i*2-1
    impares = [str(num) for num in range(1, i*2) if num % 2 == 1]
    # Une los números impares en una cadena separados por espacios
    impares_str = " ".join(impares)
    # Imprime la cadena de números impares con un relleno de espacios para formar un triángulo rectángulo
    print("{:^{}}".format(impares_str, num*2-1))
