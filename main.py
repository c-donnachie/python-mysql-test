from BD.conn import DAO
from clase import Banco, CuentaBancaria, TipoCuenta


def actualizarCuentas():
    cuentas = dao.listarCuentas()
    banco.cuentas = []
    for cuenta_data in cuentas:
        tipo = TipoCuenta(cuenta_data["tipo"], cuenta_data["descripcion"])
        cuenta_bancaria = CuentaBancaria(
            cuenta_data["titular"], tipo, cuenta_data["saldo"]
        )
        cuenta_bancaria.numero = cuenta_data["numero"]
        banco.cuentas.append(cuenta_bancaria)


def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1. Listar cuentas")
            print("2. Ingresar dinero a una cuenta")
            print("3. Retirar dinero de una cuenta")
            print("4. Eliminar una cuenta")
            print("5. Crear una nueva cuenta")
            print("6. Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                continuar = False
                print("¡Gracias por usar el sistema bancario!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    if opcion == 1:
        if len(banco.cuentas) > 0:
            banco.listar_cuentas()
        else:
            print("No se encontraron cuentas...")
    elif opcion == 2:
        if len(banco.cuentas) > 0:
            indice = int(
                input("Ingrese el índice de la cuenta a la que desea ingresar dinero: ")
            )
            cantidad = float(input("Ingrese la cantidad a ingresar: "))
            banco.ingresar_dinero(indice, cantidad)
        else:
            print("No se encontraron cuentas...")
    elif opcion == 3:
        if len(banco.cuentas) > 0:
            indice = int(
                input("Ingrese el índice de la cuenta de la que desea retirar dinero: ")
            )
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            banco.retirar_dinero(indice, cantidad)
        else:
            print("No se encontraron cuentas...")
    elif opcion == 4:
        if len(banco.cuentas) > 0:
            indice = int(input("Ingrese el índice de la cuenta que desea eliminar: "))
            banco.eliminar_cuenta(indice)
        else:
            print("No se encontraron cuentas...")
    elif opcion == 5:
        titular = input("Ingrese el titular de la nueva cuenta: ")
        tipo = TipoCuenta(
            1, "Tipo de cuenta"
        )  # Debes proporcionar los valores correctos aquí
        saldo = float(input("Ingrese el saldo inicial de la nueva cuenta: "))
        cuenta_nueva = CuentaBancaria(titular, tipo, saldo)
        banco.crear_cuenta(cuenta_nueva)
    else:
        print("Opción no válida...")


banco = Banco()
dao = DAO()
actualizarCuentas()  # Cargamos los datos de la BD en el objeto Banco
menuPrincipal()
