import hashlib


class CuentaBancaria:
    def __init__(self, id, titular, tipo, numero, saldo, usuario_id):
        self.id = id
        self.titular = titular
        self.tipo = tipo
        self.numero = numero
        self.saldo = saldo
        self.usuario_id = usuario_id


class Banco:
    def __init__(self):
        self.cuentas = []

    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(
                f"ID: {cuenta.id}, Titular: {cuenta.titular}, Tipo: {cuenta.tipo}, Saldo: {cuenta.saldo}"
            )

    def ingresar_dinero(self, id_cuenta, monto):
        if self.cuentas is None:
            print("Error: No se han cargado las cuentas desde la base de datos.")
            return

        for cuenta in self.cuentas:
            if cuenta.id == id_cuenta:
                cuenta.saldo += monto
                print(
                    f"Se ingresaron {monto} a la cuenta {cuenta.id}. Nuevo saldo: {cuenta.saldo}"
                )
                return

        print(f"No se encontró la cuenta con ID {id_cuenta}.")

    def retirar_dinero(self, id_cuenta, monto):
        for cuenta in self.cuentas:
            if cuenta.id == id_cuenta:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    print(
                        f"Se retiraron {monto} de la cuenta {cuenta.id}. Nuevo saldo: {cuenta.saldo}"
                    )
                else:
                    print("Saldo insuficiente.")
                return
        print(f"No se encontró la cuenta con ID {id_cuenta}.")

    def eliminar_cuenta(self, id_cuenta):
        for cuenta in self.cuentas:
            if cuenta.id == id_cuenta:
                self.cuentas.remove(cuenta)
                print(f"Se eliminó la cuenta con ID {id_cuenta}.")
                return
        print(f"No se encontró la cuenta con ID {id_cuenta}.")

    def crear_cuenta(self, titular, tipo, saldo):
        nuevo_id = len(self.cuentas) + 1
        nueva_cuenta = CuentaBancaria(nuevo_id, titular, tipo, saldo)
        self.cuentas.append(nueva_cuenta)
        print(f"Se creó una nueva cuenta con ID {nuevo_id}.")
