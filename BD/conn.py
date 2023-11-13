from mysql.connector import Error
from database import Database
from termcolor import colored


class DAO:
    def __init__(self):
        self.db = Database()

    def imprimir_estado_cuenta(self, id_cuenta):
        if self.db.connection.is_connected():
            try:
                cursor = self.db.connection.cursor()
                sql = "SELECT * FROM Cuentas_bancarias WHERE ID = %s"
                cursor.execute(sql, (id_cuenta,))
                resultado = cursor.fetchone()

                if resultado:
                    id_cuenta = resultado[0]
                    titular = resultado[1]
                    tipo = resultado[2]
                    numero = resultado[3]
                    saldo = resultado[4]

                    print("Estado de la cuenta:")
                    print(
                        f"ID: {id_cuenta}, Titular: {titular}, Tipo: {tipo}, Numero: {numero} , Saldo: {saldo}"
                    )
                else:
                    print(f"No se encontró la cuenta con ID {id_cuenta}.")

            except Error as ex:
                print(f"Error al intentar la conexión: {ex}")

    def listar_cuentas(self):
        if self.db.connection.is_connected():
            try:
                cursor = self.db.connection.cursor()
                cursor.execute("SELECT * FROM Cuentas_bancarias")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def ingresar_dinero(self, id_cuenta, monto):
        if self.db.connection.is_connected():
            try:
                cursor = self.db.connection.cursor()
                sql = "UPDATE Cuentas_bancarias SET Saldo = Saldo + %s WHERE ID = %s"
                cursor.execute(sql, (monto, id_cuenta))
                self.db.connection.commit()
                print(colored("¡Dinero ingresado a la cuenta!\n", "light_cyan"))
            except Error as ex:
                print("Error al intentar ingresar dinero a la cuenta: {0}".format(ex))
            finally:
                if self.db.connection.is_connected():
                    cursor.close()

    def retirar_dinero(self, id_cuenta, monto):
        if self.db.connection.is_connected():
            try:
                cursor = self.db.connection.cursor()
                sql = "UPDATE Cuentas_bancarias SET Saldo = Saldo - %s WHERE ID = %s"
                cursor.execute(sql, (monto, id_cuenta))
                self.db.connection.commit()
                print(colored("¡Dinero retirado a la cuenta!\n", "light_cyan"))
            except Error as ex:
                print("Error al intentar retirar dinero a la cuenta: {0}".format(ex))
            finally:
                if self.db.connection.is_connected():
                    cursor.close()

    def eliminar_cuenta(self, id_cuenta):
        if self.db.connection.is_connected():
            try:
                cursor = self.db.connection.cursor()
                sql = "DELETE FROM Cuentas_bancarias WHERE ID = {0}"
                cursor.execute(sql.format(id_cuenta))
                self.db.connection.commit()
                print(colored("¡Cuenta eliminada!\n", "light_cyan"))
            except Error as error:
                print("Fallo al intentar eliminar cuenta: {}".format(error))
                self.db.connection.rollback()
            finally:
                if self.db.connection.is_connected():
                    cursor.close()

    def crear_cuenta(self, titular, tipo, saldo):
        try:
            cursor = self.db.connection.cursor()

            cursor.execute("SELECT MAX(id) FROM Cuentas_bancarias")
            max_id = cursor.fetchone()[0]
            nuevo_id = 1 if max_id is None else max_id + 1

            nuevo_numero = nuevo_id * 87

            sql = "INSERT INTO Cuentas_bancarias (id, Titular, Tipo, Saldo, Numero) VALUES (%s, %s, %s, %s, %s)"
            values = (nuevo_id, titular, tipo, saldo, nuevo_numero)
            cursor.execute(sql, values)
            self.db.connection.commit()
            print(
                colored(
                    f"Se creó una nueva cuenta con ID {nuevo_id} y número {nuevo_numero}.",
                    "light_cyan",
                )
            )
        except Error as ex:
            print("Error al intentar crear la cuenta: {0}".format(ex))
        finally:
            if self.db.connection.is_connected():
                cursor.close()
