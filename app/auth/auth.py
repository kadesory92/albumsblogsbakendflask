import jwt
# import jwt
from datetime import datetime, timedelta
from flask import request, jsonify, current_app
from functools import wraps
from app.models.user import User


class Auth:
    @staticmethod
    def generate_token(user_id):
        """
        Génère un token JWT pour un utilisateur donné.
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1),  # Expire dans 1 jour
                'iat': datetime.utcnow(),  # Timestamp de génération
                'sub': user_id  # ID de l'utilisateur comme sujet
            }
            return jwt.encode(
                payload,
                current_app.config.get('JWT_SECRET_KEY '),
                algorithm='HS256'
            )
        except Exception as e:
            return str(e)

    @staticmethod
    def decode_token(token):
        """
        Décode le token JWT et récupère l'ID de l'utilisateur (sub).
        """
        try:
            payload = jwt.decode(token, current_app.config.get('JWT_SECRET_KEY '), algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def login_required(f):
        """
        Décorateur pour protéger les routes nécessitant une authentification.
        """

        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]
            if not token:
                return jsonify({'message': 'Token is missing!'}), 403

            try:
                user_id = Auth.decode_token(token)
                current_user = User.query.get(user_id)
                if not current_user:
                    return jsonify({'message': 'User not found!'}), 403
            except Exception as e:
                return jsonify({'message': str(e)}), 403

            return f(current_user, *args, **kwargs)

        return decorated_function



