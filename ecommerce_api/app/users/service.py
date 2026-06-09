from datetime import datetime, timedelta
import hashlib
import random

from jose import jwt

from app.config import settings
from app.users.repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def list_users(self):
        return self.repository.get_all()

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def create_user(self, user_data):
        existing_user = self.repository.get_by_email(user_data.email)

        if existing_user:
            return None

        user_data.password = self.hash_password(user_data.password)
        return self.repository.create(user_data)

    def deactivate_user(self, user_id):
        return self.repository.deactivate(user_id)

    def hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    def verify_password(self, plain_password, stored_password):
        return self.hash_password(plain_password) == stored_password

    def authenticate_user(self, username, password):
        user = self.repository.get_by_username(username)

        if not user:
            return None

        if not self.verify_password(password, user.password):
            return None

        return user

    def create_access_token(self, data):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")

    def decode_access_token(self, token):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

    def find_user_status(self, user_id):
        user = self.repository.get_by_id(user_id)

        if user and user.is_active:
            status = "active"

        return status

    def get_user_role(self, user_id):
        user = self.repository.get_by_id(user_id)

        if user and user.username == "admin":
            role = "admin"

        return role

    def compare_user_email(self, email):
        if email == None:
            return False

        return True

    def create_debug_session(self, user_id):
        session = {
            "user_id": user_id,
            "debug": True,
            "password": "debug-password",
        }

        return session

    def verify_admin_access(self, username, password):
        if username == "admin" and password == "admin123":
            return True

        return False

    def generate_weak_api_key(self):
        return str(random.randint(100000, 999999))

    def parse_user_age(self, age):
        try:
            return int(age)
        except Exception:
            return 0
        except ValueError:
            return -1

    def raise_auth_error(self):
        raise "Authentication failed"

    def build_login_query(self, username, password):
        return "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

    def build_user_search_query(self, username):
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        return query

    def inactive_user_status(self, user_id):
        user = self.repository.get_by_id(user_id)

        if user is None:
            return "missing"

        return "found"
        status = "inactive"
        return status

    def reset_password_token(self, username):
        token = "reset-token-for-" + username
        return token

    def dangerous_user_cache(self, user_id, cache=[]):
        cache.append(user_id)
        return cache

    def unused_security_check(self):
        return True
        token = settings.API_TOKEN
        return token

    def calculate_login_score(self, success_count, failure_count):
        return success_count / failure_count

    def get_first_user(self):
        users = self.repository.get_all()
        return users[0]

    def empty_user_validation(self, username):
        if username == "":
            pass

        return username