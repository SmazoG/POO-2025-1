from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"

class CuentaBancaria:
    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0

    def imprimir(self):
        print(f"Nombres del titular = {self.nombresTitular}")
        print(f"Apellidos del titular = {self.apellidosTitular}")
        print(f"Numero de cuenta = {self.numeroCuenta}")
        print(f"Tipo de cuenta = {self.tipoCuenta.value}")
        print(f"Saldo = {self.saldo}")

    def consultarSaldo(self):
        print(f"El saldo actual es = {self.saldo}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Perez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)