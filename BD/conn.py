import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_database = os.getenv("DB_DATABASE")


class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_pass,
                database=db_database,
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def imprimir_estado_cuenta(self, id_cuenta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
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
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Cuentas_bancarias")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def ingresar_dinero(self, id_cuenta, monto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE Cuentas_bancarias SET Saldo = Saldo + {0} WHERE ID = {1}"
                cursor.execute(sql.format(monto, id_cuenta))
                self.conexion.commit()
                print("¡Dinero ingresado a la cuenta!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def retirar_dinero(self, id_cuenta, monto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE Cuentas_bancarias SET Saldo = Saldo - {0} WHERE ID = {1} AND Saldo >= {0}"
                cursor.execute(sql.format(monto, id_cuenta))
                self.conexion.commit()
                print("¡Dinero retirado de la cuenta!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminar_cuenta(self, id_cuenta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM Cuentas_bancarias WHERE ID = {0}"
                cursor.execute(sql.format(id_cuenta))
                self.conexion.commit()
                print("¡Cuenta eliminada!\n")
            except Error as error:
                print("Fallo al intentar eliminar cuenta: {}".format(error))
                self.conexion.rollback()
            finally:
                if self.conexion.is_connected():
                    cursor.close()

    def crear_cuenta(self, titular, tipo, saldo):
        try:
            cursor = self.conexion.cursor()

            # Obtener el último ID de cuentas para calcular el nuevo ID
            cursor.execute("SELECT MAX(id) FROM Cuentas_bancarias")
            max_id = cursor.fetchone()[0]
            nuevo_id = 1 if max_id is None else max_id + 1

            nuevo_numero = nuevo_id * 87

            sql = "INSERT INTO Cuentas_bancarias (id, Titular, Tipo, Saldo, Numero) VALUES (%s, %s, %s, %s, %s)"
            values = (nuevo_id, titular, tipo, saldo, nuevo_numero)
            cursor.execute(sql, values)
            self.conexion.commit()
            print(
                f"Se creó una nueva cuenta con ID {nuevo_id} y número {nuevo_numero}."
            )
        except Error as ex:
            print("Error al intentar crear la cuenta: {0}".format(ex))
        finally:
            if self.conexion.is_connected():
                cursor.close()
