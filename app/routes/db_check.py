# app/routes/db_check.py

from flask import Blueprint, jsonify
from app.db_test import test_db_connection  # Adjust import as needed

db_check_bp = Blueprint('db_check', __name__)

@db_check_bp.route('/db-check', methods=['GET'])
def db_check():
    success = test_db_connection()
    return jsonify({"database_connection": "ok" if success else "failed"})
