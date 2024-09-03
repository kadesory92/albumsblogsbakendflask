from flask import request, jsonify

from app.auth import Auth
from app.schemas.user_schema import user_schema
from app.services import UserService

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Vérifiez si 'data' est un dictionnaire
    if not isinstance(data, dict):
        return jsonify({'message': 'Invalid data format, expected a JSON object'}), 400

    # Vérifiez si tous les champs requis sont présents
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user, success = UserService.register_user(username, email, password)
    if not success:
        return jsonify(user_schema.dump(user)), 400

    token = Auth.generate_token(user.id)
    return jsonify({'message': 'User registered successfully', 'token': token}), 201


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400

    username = data.get('username')
    password = data.get('password')

    user = UserService.authenticate(username, password)
    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    token = Auth.generate_token(user.id)
    return jsonify({'message': 'Logged successfully', 'token': token}), 200


