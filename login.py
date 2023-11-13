from database import Database
import hashlib


class Login:
    def __init__(self):
        self.db = Database()

    def iniciar_sesion(self, username, password):
        user_id = self.db.verify_user(username, password)
        return user_id

    def registrar_usuario(self, username, password):
        hashed_password = self._hash_password(password)
        new_user = User(username, hashed_password)
        new_user.save_to_db()

    @staticmethod
    def _hash_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest()
