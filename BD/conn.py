import mysql.connector
from mysql.connector import Error


class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=8889,
                user="donnachie",
                password="",
                database="banco_db",
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarCuentas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Cuentas_bancarias")
                cuentas = cursor.fetchall()
                cursor.close()
                return cuentas
            except Error as ex:
                print("Error al listar las cuentas: {0}".format(ex))

    def ingresarDinero(self, indice, cantidad):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    "UPDATE Cuentas_bancarias SET saldo = saldo + %s WHERE id = %s",
                    (cantidad, indice),
                )
                self.conexion.commit()
                cursor.close()
                return True
            except Error as ex:
                print("Error al ingresar dinero: {0}".format(ex))
                return False
