from BD.conn import DAO
from clase import Banco, CuentaBancaria
import os

contador = 0


# Mis variables
def limpiarContar():
    limpiar_consola()
    global contador
    contador = contador + 1


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

    # Limpiamos las cuentas existentes en el objeto banco
    banco.cuentas = []

    for cuenta_bd in cuentas_bd:
        nuevo_id = cuenta_bd[0]
        titular = cuenta_bd[1]
        tipo = cuenta_bd[2]
        numero = cuenta_bd[3]
        saldo = cuenta_bd[4]

        # Creamos una nueva instancia de CuentaBancaria
        nueva_cuenta = CuentaBancaria(nuevo_id, titular, tipo, numero, saldo)

        # Usamos el método crear_cuenta del objeto banco con la nueva instancia
        banco.crear_cuenta1(nueva_cuenta)


def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            if contador == 0:
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
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 0:
                continuar = False
                print("¡Gracias por usar la aplicación de banco!")
                break
            else:
                opcion_correcta = True
                ejecutar_opcion(opcion)


def ejecutar_opcion(opcion):
    if opcion == 1:
        limpiarContar()
        limpiar_consola()
        actualizar_cuentas()
        banco.listar_cuentas()
    elif opcion == 2:
        limpiarContar()
        limpiar_consola()
        actualizar_cuentas()
        banco.listar_cuentas()
        id_cuenta = int(input("Ingrese el ID de la cuenta: "))
        monto = float(input("Ingrese la cantidad a depositar: "))
        limpiar_consola()
        dao.ingresar_dinero(id_cuenta, monto)
        dao.imprimir_estado_cuenta(id_cuenta)
    elif opcion == 3:
        limpiarContar()
        limpiar_consola()
        id_cuenta = int(input("Ingrese el ID de la cuenta: "))
        monto = float(input("Ingrese la cantidad a retirar: "))
        limpiar_consola()
        dao.retirar_dinero(id_cuenta, monto)
        dao.imprimir_estado_cuenta(id_cuenta)
    elif opcion == 4:
        id_cuenta = int(input("Ingrese el ID de la cuenta a eliminar: "))
        dao.eliminar_cuenta(id_cuenta)
    elif opcion == 5:
        titular = input("Ingrese el titular de la cuenta: ")
        tipo = input("Ingrese el tipo de cuenta: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        dao.crear_cuenta(titular, tipo, saldo)
        actualizar_cuentas()


# Creamos instancias de las clases
dao = DAO()
banco = Banco()

# Actualizamos las cuentas desde la base de datos al objeto banco
actualizar_cuentas()

# Ejecutamos el menú principal
menu_principal()
