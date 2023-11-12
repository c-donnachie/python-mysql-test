import mysql.connector
from mysql.connector import Error
from clase import CuentaBancaria

import os
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_database = os.getenv("DB_DATABASE")


class BancoDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_pass,
            database=db_database,
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def listar_cuentas(self):
        query = "SELECT * FROM Cuentas_bancarias"
        self.cursor.execute(query)
        cuentas_en_bd = self.cursor.fetchall()
        for cuenta_bd in cuentas_en_bd:
            cuenta = CuentaBancaria(*cuenta_bd)
            print(
                f"ID: {cuenta.id}, Titular: {cuenta.titular}, Tipo: {cuenta.tipo}, Saldo: {cuenta.saldo}"
            )

    def ingresar_dinero(self, id_cuenta, monto):
        query = "SELECT * FROM Cuentas_bancarias WHERE id = %s"
        self.cursor.execute(query, (id_cuenta,))
        cuenta_bd = self.cursor.fetchone()
        if cuenta_bd:
            nuevo_saldo = cuenta_bd[3] + monto
            update_query = "UPDATE Cuentas_bancarias SET saldo = %s WHERE id = %s"
            self.cursor.execute(update_query, (nuevo_saldo, id_cuenta))
            self.connection.commit()
            print(
                f"Se ingresaron {monto} a la cuenta {id_cuenta}. Nuevo saldo: {nuevo_saldo}"
            )
        else:
            print(f"No se encontró la cuenta con ID {id_cuenta}.")

    def retirar_dinero(self, id_cuenta, monto):
        query = "SELECT * FROM Cuentas_bancarias WHERE id = %s"
        self.cursor.execute(query, (id_cuenta,))
        cuenta_bd = self.cursor.fetchone()
        if cuenta_bd:
            if cuenta_bd[3] >= monto:
                nuevo_saldo = cuenta_bd[3] - monto
                update_query = "UPDATE Cuentas_bancarias SET saldo = %s WHERE id = %s"
                self.cursor.execute(update_query, (nuevo_saldo, id_cuenta))
                self.connection.commit()
                print(
                    f"Se retiraron {monto} de la cuenta {id_cuenta}. Nuevo saldo: {nuevo_saldo}"
                )
            else:
                print("Saldo insuficiente.")
        else:
            print(f"No se encontró la cuenta con ID {id_cuenta}.")

    def eliminar_cuenta(self, id_cuenta):
        delete_query = "DELETE FROM Cuentas_bancarias WHERE id = %s"
        self.cursor.execute(delete_query, (id_cuenta,))
        self.connection.commit()
        print(f"Se eliminó la cuenta con ID {id_cuenta}.")

    def crear_cuenta(self, titular, tipo, saldo):
        insert_query = (
            "INSERT INTO Cuentas_bancarias (titular, tipo, saldo) VALUES (%s, %s, %s)"
        )
        values = (titular, tipo, saldo)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("Se creó una nueva cuenta.")
