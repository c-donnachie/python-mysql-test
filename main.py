# main.py
from clase import Banco
from BD.conn import DAO
from decimal import Decimal
from user import User, Database
import os
from termcolor import colored

contador = False
username = ""
escribir = ">>"


def limpiarContar():
    limpiar_consola()
    global contador
    contador = True


def printMenuPrincipal():
    print(
        colored(
            "╔════════════════ ** MENÚ PRINCIPAL ** ════════════════╗",
            "light_magenta",
        )
    )
    print(colored(f"║ Usuario: {username}", "light_magenta"))
    print(colored("║", "light_magenta"))
    print(colored("║", "light_magenta") + colored(" 1.- Listar cuentas", "green"))
    print(
        colored("║", "light_magenta")
        + colored(" 2.- Ingresar dinero a cuenta", "green")
    )
    print(
        colored("║", "light_magenta")
        + colored(" 3.- Retirar dinero de cuenta", "green")
    )
    print(colored("║", "light_magenta") + colored(" 4.- Eliminar cuenta", "green"))
    print(colored("║", "light_magenta") + colored(" 5.- Crear nueva cuenta", "green"))
    print(colored("║", "light_magenta") + colored(" 0.- Salir", "green"))
    print(
        colored(
            "╚══════════════════════════════════════════════════════╝",
            "light_magenta",
        )
    )


def printMenuLogin():
    print(
        colored(
            "╔════════════ LOGIN  ════════════╗",
            "light_green",
        )
    )
    print(colored("║", "light_green"))
    print(colored("║", "light_green") + colored(" 1.- Iniciar sesión", "green"))
    print(colored("║", "light_green") + colored(" 2.- Registrarse", "green"))
    print(colored("║", "light_green"))
    print(
        colored(
            "╚════════════════════════════════╝",
            "light_green",
        )
    )


def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == "posix":
        os.system("clear")
    elif sistema_operativo == "nt":
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
        banco.inicializar_cuentas(id_cuenta, titular, tipo, numero, saldo)


def login():
    while True:
        limpiar_consola()
        printMenuLogin()
        choice = input(f"Seleccione una opción {escribir} ")

        if choice == "1":
            global username
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")

            user = User(username, password)
            user_id = user.authenticate()
            if user_id:
                print(f"Inicio de sesión exitoso. Usuario ID: {user_id}")
                return True
            else:
                print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")

        elif choice == "2":
            username = input(f"Nombre de usuario {escribir} ")
            password = input(f"Contraseña {escribir} ")

            new_user = User(username, password)
            new_user.save_to_db()
            print("Usuario registrado exitosamente.")
            return True

        print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")


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
        id_cuenta = int(input(f"Ingrese el ID de la cuenta {escribir} "))
        monto = Decimal(input(f"Ingrese la cantidad a retirar {escribir} "))
        limpiarContar()
        if banco.retirar_dinero(id_cuenta, monto):
            dao.retirar_dinero(id_cuenta, monto)
    elif opcion == 4:
        limpiarContar()
        banco.listar_cuentas()
        id_cuenta = int(input(f"Ingrese el ID de la cuenta a eliminar {escribir} "))
        banco.eliminar_cuenta(id_cuenta)
        dao.eliminar_cuenta(id_cuenta)
    elif opcion == 5:
        limpiarContar()
        titular = input(f"Ingrese el titular de la cuenta {escribir} ")
        print("Tipos de cuenta:")
        print("1. Cuenta Vista")
        print("2. Cuenta Corriente")
        while True:
            tipo = input(f"Ingrese el tipo de cuenta {escribir} ")
            if tipo == "1":
                tipo = "Cuenta Vista"
                break
            elif tipo == "2":
                tipo = "Cuenta Corriente"
                break
            else:
                print("Opcion invalida!")
        saldo = Decimal(input(f"Ingrese el saldo inicial {escribir} "))
        banco.crear_cuenta(titular, tipo, saldo)
        dao.crear_cuenta(titular, tipo, saldo)


def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            try:
                if contador == False:
                    limpiar_consola()
                printMenuPrincipal()
                opcion = int(input(f"Seleccione una opción {escribir} "))

                if opcion < 0 or opcion > 5:
                    pass
                elif opcion == 0:
                    continuar = False
                    limpiar_consola()
                    print("¡Gracias por usar la aplicación del banco!")
                    break
                else:
                    opcion_correcta = True
                    ejecutar_opcion(opcion)

            except ValueError:
                pass


dao = DAO()
banco = Banco()

actualizar_cuentas()

if login():
    menu_principal()
