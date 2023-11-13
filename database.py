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

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def fetch_one(self, query, values=None):
        self.execute_query(query, values)
        return self.cursor.fetchone()

    def fetch_all(self, query, values=None):
        self.execute_query(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
