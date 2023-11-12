from clase import Banco
from BD.conn import BancoDAO


def main():
    banco = Banco()
    dao = BancoDAO()

    # Actualizar el objeto 'banco' con los datos de la base de datos
    # banco.cuentas = dao.listar_cuentas()

    while True:
        print("\nMenú:")
        print("1. Listar cuentas")
        print("2. Ingresar dinero a cuenta")
        print("3. Retirar dinero de cuenta")
        print("4. Eliminar cuenta")
        print("5. Crear nueva cuenta")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            banco.cuentas = dao.listar_cuentas()
        elif opcion == "2":
            id_cuenta = int(input("Ingrese el ID de la cuenta: "))
            monto = float(input("Ingrese la cantidad a depositar: "))
            banco.ingresar_dinero(id_cuenta, monto)
        elif opcion == "3":
            id_cuenta = int(input("Ingrese el ID de la cuenta: "))
            monto = float(input("Ingrese la cantidad a retirar: "))
            banco.retirar_dinero(id_cuenta, monto)
        elif opcion == "4":
            id_cuenta = int(input("Ingrese el ID de la cuenta a eliminar: "))
            banco.eliminar_cuenta(id_cuenta)
        elif opcion == "5":
            titular = input("Ingrese el titular de la cuenta: ")
            tipo = input("Ingrese el tipo de cuenta: ")
            saldo = float(input("Ingrese el saldo inicial: "))
            banco.crear_cuenta(titular, tipo, saldo)
        elif opcion == "0":
            dao.close_connection()
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
