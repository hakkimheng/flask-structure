from flask import Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Root endpoint"""
    pass


@main_bp.route('/health')
def health():
    """Health check endpoint"""
    pass

