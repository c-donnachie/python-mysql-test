from decimal import Decimal


class CuentaBancaria:
    def __init__(self, id, titular, tipo, numero, saldo):
        self.id = id
        self.titular = titular
        self.tipo = tipo
        self.numero = numero
        self.saldo = saldo

    def returnArray(self):
        return [self.id, self.titular, self.tipo, self.numero, self.saldo]


class Banco:
    def __init__(self):
        self.cuentas = []

    def buscar_cuenta_por_id(self, id_cuenta):
        for cuenta in self.cuentas:
            if cuenta.id == id_cuenta:
                return cuenta
        return None

    def inicializar_cuentas(self, id, titular, tipo, numero, saldo):
        nueva_cuenta = CuentaBancaria(id, titular, tipo, numero, saldo)
        self.cuentas.append(nueva_cuenta)

    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(
                f"ID: {cuenta.id}, Titular: {cuenta.titular}, Tipo: {cuenta.tipo}, Numero: {cuenta.numero} , Saldo: {cuenta.saldo}"
            )

    def crear_cuenta(self, titular, tipo, saldo):
        nuevo_id = len(self.cuentas) + 1
        nuevo_numero = nuevo_id * 87
        nueva_cuenta = CuentaBancaria(nuevo_id, titular, tipo, nuevo_numero, saldo)
        self.cuentas.append(nueva_cuenta)
        print(f"✓ Se creó una nueva cuenta con ID {nuevo_id}.")

    def ingresar_dinero(self, id_cuenta, monto):
        cuenta = self.buscar_cuenta_por_id(id_cuenta)
        if cuenta:
            cuenta.saldo += Decimal(str(monto))
            print(
                f"Se ingresaron {monto} a la cuenta {cuenta.id}. Nuevo saldo: {cuenta.saldo}"
            )
            return True
        else:
            print(f"No se encontró la cuenta con ID {id_cuenta}.")
            return False

    def retirar_dinero(self, id_cuenta, monto):
        cuenta = self.buscar_cuenta_por_id(id_cuenta)
        if cuenta:
            if cuenta.saldo >= monto:
                cuenta.saldo -= Decimal(str(monto))
                print(
                    f"Se retiraron {monto} de la cuenta {cuenta.id}. Nuevo saldo: {cuenta.saldo}"
                )
                return True
            else:
                print(
                    "Saldo insuficiente. No se puede retirar más dinero del disponible."
                )
                return False
        else:
            print(f"No se encontró la cuenta con ID {id_cuenta}.")
            return False

    def eliminar_cuenta(self, id_cuenta):
        cuenta = self.buscar_cuenta_por_id(id_cuenta)
        if cuenta:
            self.cuentas.remove(cuenta)
            print(f"✘ Se eliminó la cuenta con ID {id_cuenta}.")
        else:
            print(f"No se encontró la cuenta con ID {id_cuenta}.")


if __name__ == "__main__":
    banco = Banco()
    # banco.agregar_cuenta("Titular de Prueba 1", "Cuenta Corriente", 1000)
    # banco.agregar_cuenta("Titular de Prueba 2", "Cuenta de Ahorro", 500)
    # banco.listar_cuentas()

    # # Ejemplo de operaciones
    # banco.ingresar_dinero(1, 200)
    # banco.retirar_dinero(2, 100)
    # banco.eliminar_cuenta(1)

    # banco.listar_cuentas()
