import mysql.connector
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_database = os.getenv("DB_DATABASE")


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_pass,
            database=db_database,
        )
        self.cursor = self.connection.cursor()

    def verify_user(self, username, password):
        query = "SELECT id, password FROM usuarios WHERE username = %s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()

        if result:
            user_id, hashed_password = result
            if self.check_password(password, hashed_password):
                return user_id
        return None

    # pass codificada
    def check_password(self, password, hashed_password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest() == hashed_password

    def close(self):
        self.cursor.close()
        self.connection.close()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self, database):
        md5 = hashlib.md5()
        md5.update(self.password.encode("utf-8"))
        hashed_password = md5.hexdigest()
        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        values = (self.username, hashed_password)
        database.cursor.execute(query, values)
        database.connection.commit()


def main():
    database = Database()

    print("1. Iniciar sesión")
    print("2. Registrarse")
    choice = input("Seleccione una opción: ")

    if choice == "1":
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        user_id = database.verify_user(username, password)
        if user_id:
            print(f"Inicio de sesión exitoso. Usuario ID: {user_id}")
        else:
            print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")

    elif choice == "2":
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        new_user = User(username, password)
        new_user.save_to_db(database)
        print("Usuario registrado exitosamente.")

    database.close()


if __name__ == "__main__":
    main()
