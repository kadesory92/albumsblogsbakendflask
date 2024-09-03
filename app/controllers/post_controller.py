from flask import request, jsonify, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.schemas.post_schema import post_schema
from app.services import PostService

post_blueprint = Blueprint('posts', __name__)


@post_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()

    # Vérifiez si 'data' est un dictionnaire
    if not isinstance(data, dict):
        return jsonify({'message': 'Invalid data format, expected a JSON object'}), 400

    # Vérifiez si tous les champs requis sont présents
    if not data.get('title') or not data.get('content'):
        return jsonify({'message': 'Missing required fields'}), 400

    title = data.get('title')
    content = data.get('content')
    user_id = get_jwt_identity()

    post, success = PostService.create_post(title, content, user_id)
    if not success:
        return jsonify(post_schema.dump(post)), 400

    return jsonify({'message': 'User registered successfully'}), 201



