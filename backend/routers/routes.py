from flask import Blueprint, jsonify
from sqlalchemy import text

from core.config import ENVIRONMENT
from db.database import db

from core.middleware import require_bearer_token


bp = Blueprint('/api/v1', __name__, url_prefix='/api/v1')


@bp.route('/', methods=['GET'])
# @require_bearer_token
def read_root():
    return jsonify({
        'msg': 'cloaktest'
    }), 200

# TODO DELETE
# Ruta para probar la conexión a la base de datos
if ENVIRONMENT == 'development':
    @bp.route('/test_db_connection', methods=['GET'])
    def test_db_connection():
        try:
            db.session.execute(text('SELECT 1'))
            return jsonify("Database connection successful!"), 200
        except Exception as e:
            import traceback
            return jsonify({
                "error": f"Database connection failed: {e}",
                "traceback": traceback.format_exc()
            }), 500
