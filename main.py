from clase import Banco, CuentaBancaria
from BD.conn import DAO
from decimal import Decimal
import os

contador = False


# Mis variables
def limpiarContar():
    limpiar_consola()
    global contador
    contador = True


def limpiar_consola():
    sistema_operativo = os.name

    if sistema_operativo == "posix":  # Para sistemas basados en Unix (Linux, macOS)
        os.system("clear")
    elif sistema_operativo == "nt":  # Para Windows
        os.system("cls")
    else:
        print("No se pudo determinar el sistema operativo.")


def actualizar_cuentas():
    cuentas_bd = dao.listar_cuentas()

    banco.cuentas = []

    for cuenta_bd in cuentas_bd:
        id_cuenta = cuenta_bd[0]
        titular = cuenta_bd[1]
        tipo = cuenta_bd[2]
        numero = cuenta_bd[3]
        saldo = cuenta_bd[4]

        # nueva_cuenta = CuentaBancaria(id_cuenta, titular, tipo, numero, saldo)

        banco.inicializar_cuentas(id_cuenta, titular, tipo, numero, saldo)


def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            try:
                if contador == False:
                    limpiar_consola()
                print("==================== MENÚ PRINCIPAL ====================")
                print("1.- Listar cuentas")
                print("2.- Ingresar dinero a cuenta")
                print("3.- Retirar dinero de cuenta")
                print("4.- Eliminar cuenta")
                print("5.- Crear nueva cuenta")
                print("0.- Salir")
                print("========================================================")
                opcion = int(input("Seleccione una opción: "))

                if opcion < 0 or opcion > 5:
                    pass
                elif opcion == 0:
                    continuar = False
                    print("¡Gracias por usar la aplicación de banco!")
                    break
                else:
                    opcion_correcta = True
                    ejecutar_opcion(opcion)

            except ValueError:
                pass


def ejecutar_opcion(opcion):
    if opcion == 1:
        limpiarContar()
        banco.listar_cuentas()
    elif opcion == 2:
        limpiarContar()
        banco.listar_cuentas()
        id_cuenta = int(input("Ingrese el ID de la cuenta: "))
        monto = Decimal(input("Ingrese la cantidad a depositar: "))
        limpiarContar()
        if banco.ingresar_dinero(id_cuenta, monto):
            dao.ingresar_dinero(id_cuenta, monto)
    elif opcion == 3:
        limpiarContar()
        banco.listar_cuentas()
        id_cuenta = int(input("Ingrese el ID de la cuenta: "))
        monto = Decimal(input("Ingrese la cantidad a retirar: "))
        limpiarContar()
        if banco.retirar_dinero(id_cuenta, monto):
            dao.retirar_dinero(id_cuenta, monto)
    elif opcion == 4:
        limpiarContar()
        banco.listar_cuentas()
        id_cuenta = int(input("Ingrese el ID de la cuenta a eliminar: "))
        banco.eliminar_cuenta(id_cuenta)
        dao.eliminar_cuenta(id_cuenta)
    elif opcion == 5:
        limpiarContar()
        titular = input("Ingrese el titular de la cuenta: ")
        print("Tipos de cuenta:")
        print("1. Cuenta Vista")
        print("2. Cuenta Corriente")
        while True:
            tipo = input("Ingrese el tipo de cuenta: ")
            if tipo == "1":
                tipo = "Cuenta Vista"
                break
            elif tipo == "2":
                tipo = "Cuenta Corriente"
                break
            else:
                print("Opcion invalida!")
        saldo = Decimal(input("Ingrese el saldo inicial: "))
        banco.crear_cuenta(titular, tipo, saldo)
        dao.crear_cuenta(titular, tipo, saldo)


# Creamos instancias de las clases
dao = DAO()
banco = Banco()

# Actualizamos las cuentas desde la base de datos al objeto banco
actualizar_cuentas()

# Ejecutamos el menú principal
menu_principal()
