class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.bitacora = []

    def depositar(self, monto):
        self.saldo += monto
        self.bitacora.append("D {}".format(monto))

    def retirar(self, monto):
        if self.saldo < monto:
            print("No tiene fondos suficientes")
        else:
            self.saldo -= monto
            self.bitacora.append("R {}".format(monto))

    def imprimir_saldo(self):
        print("Saldo final: {}".format(self.saldo))

        print("Bitácora de operaciones:")
        for operacion in self.bitacora:
            print(operacion)

cuenta = CuentaBancaria(0)

while True:
    linea = input("Introduce una operación (D para depositar, R para retirar, línea vacía para salir): ")
    if linea == "":
        cuenta.imprimir_saldo()
        break

    operacion, monto_str = linea.split()
    monto = int(monto_str)

    if operacion == "D":
        cuenta.depositar(monto)
    elif operacion == "R":
        cuenta.retirar(monto)
    else:
        print("Operación no válida")
