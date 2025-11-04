from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

# Simple in-memory storage for users and feedback
users = {}

user_auth = Blueprint('user_auth', __name__)

@user_auth.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    if username in users:
        return jsonify({'error': 'User already exists'}), 409
    users[username] = {
        'id': str(uuid.uuid4()),
        'password_hash': generate_password_hash(password),
        'preferences': {},
        'favorites': set(),
        'role': 'user'
    }
    return jsonify({'message': 'User registered successfully'})

@user_auth.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'error': 'Invalid username or password'}), 401
    # For MVP, return simple token (username)
    return jsonify({'token': username})

@user_auth.route('/api/feedback', methods=['POST'])
def feedback():
    data = request.json
    token = data.get('token')
    recipe_id = data.get('recipeId')
    rating = data.get('rating')
    comments = data.get('comments', '')
    if token not in users:
        return jsonify({'error': 'Invalid token'}), 401
    if not recipe_id or not rating:
        return jsonify({'error': 'Missing recipeId or rating'}), 400
    # Store feedback - just print/log for now
    # In real app, save to DB
    print(f"Feedback from {token}: recipe {recipe_id}, rating {rating}, comments {comments}")
    return jsonify({'message': 'Feedback received'})

@user_auth.route('/api/favorites', methods=['POST'])
def add_favorite():
    data = request.json
    token = data.get('token')
    recipe_id = data.get('recipeId')
    if token not in users:
        return jsonify({'error': 'Invalid token'}), 401
    if not recipe_id:
        return jsonify({'error': 'Missing recipeId'}), 400
    users[token]['favorites'].add(recipe_id)
    return jsonify({'message': 'Recipe added to favorites'})

@user_auth.route('/api/favorites', methods=['GET'])
def get_favorites():
    token = request.args.get('token')
    if token not in users:
        return jsonify({'error': 'Invalid token'}), 401
    favs = list(users[token]['favorites'])
    return jsonify({'favorites': favs})
