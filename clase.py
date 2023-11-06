class TipoCuenta:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion


class CuentaBancaria:
    def __init__(self, titular, tipo, saldo):
        self.titular = titular
        self.tipo = tipo
        self.numero = None
        self.saldo = saldo


class Banco:
    def __init__(self):
        self.cuentas = []

    def listar_cuentas(self):
        for indice, cuenta in enumerate(self.cuentas):
            print(
                "Índice: {0}, Titular: {1}, Tipo: {2}, Número: {3}, Saldo: {4}".format(
                    indice,
                    cuenta.titular,
                    cuenta.tipo.descripcion,
                    cuenta.numero,
                    cuenta.saldo,
                )
            )

    def ingresar_dinero(self, indice, cantidad):
        if 0 <= indice < len(self.cuentas):
            self.cuentas[indice].saldo += cantidad

    def retirar_dinero(self, indice, cantidad):
        if 0 <= indice < len(self.cuentas):
            if self.cuentas[indice].saldo >= cantidad:
                self.cuentas[indice].saldo -= cantidad
            else:
                print("Saldo insuficiente en la cuenta.")

    def eliminar_cuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            del self.cuentas[indice]

    def crear_cuenta(self, cuenta):
        cuenta.numero = len(self.cuentas) * 87
        self.cuentas.append(cuenta)
