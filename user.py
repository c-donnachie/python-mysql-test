import hashlib
from database import Database


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db = Database()
        hashed_password = self._hash_password(self.password)
        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        values = (self.username, hashed_password)
        db.execute_query(query, values)
        db.close()

    def authenticate(self):
        db = Database()
        query = "SELECT id, password FROM usuarios WHERE username = %s"
        values = (self.username,)
        result = db.fetch_one(query, values)

        if result:
            user_id, hashed_password = result
            if self.check_password(self.password, hashed_password):
                return user_id
        return None

    @staticmethod
    def _hash_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest()

    @staticmethod
    def check_password(password, hashed_password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest() == hashed_password
