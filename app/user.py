# https://boh717.github.io/post/flask-login-and-mongodb/
import bcrypt

class User():

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
        
    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.hashpw(password.encode('utf-8'), password_hash.encode('utf-8'))