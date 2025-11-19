from flask import Blueprint

api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def api_index():
    """API root endpoint"""
    pass


@api_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    pass


@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    pass


@api_bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    pass


@api_bp.route('/items', methods=['GET'])
def get_items():
    """Get all items"""
    pass


@api_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item by ID"""
    pass

