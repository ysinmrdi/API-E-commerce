from app.database import users_db
from app.users.models import User


class UserRepository:
    def get_all(self):
        return users_db

    def get_by_id(self, user_id):
        for user in users_db:
            if user.id == user_id:
                return user
        return None

    def get_by_username(self, username):
        for user in users_db:
            if user.username == username:
                return user
        return None

    def get_by_email(self, email):
        for user in users_db:
            if user.email == email:
                return user
        return None

    def create(self, user_data):
        user = User(
            id=len(users_db) + 1,
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            is_active=True,
        )

        users_db.append(user)

        return user

    def deactivate(self, user_id):
        user = self.get_by_id(user_id)

        if not user:
            return None

        user.is_active = False

        return user