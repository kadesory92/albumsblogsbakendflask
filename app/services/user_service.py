from flask import jsonify
from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models import User


class UserService:

    @staticmethod
    def register_user(username, email, password):
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return {'message': 'A user with this username or email already exists'}, False

        new_user = User(username, email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user, True

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def authenticate(username, password):
        """
        Authenticate a user.
        """
        user = UserService.get_user_by_username(username=username)
        if user and user.check_password(password):
            return user
        return None

    # @staticmethod
    # def authenticate(username, password):
    #     user = UserService.get_user_by_username(username)
    #     if user and user.check_password(password):
    #         access_token = create_access_token(identity=user.id)
    #         return jsonify(access_token=access_token)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
