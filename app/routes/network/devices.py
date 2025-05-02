from flask_restful import Resource
from flask import Blueprint, request, jsonify
from nati.config_manager import ConfigManager
from app.utils.db import get_db_connection  # or wherever you store the helper
import hashlib
import pymysql

# Load DB credentials
config = ConfigManager()

db_config = {
    'host': config.get('database.host'),
    'port': int(config.get('database.port')),
    'user': config.get('database.username'),
    'password': config.get('database.password'),
    'database': config.get('database.database')
}

def is_valid_api_key(api_key):
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM nati_api_key WHERE api_key_hash = %s AND active = 1", (key_hash,))
        return cursor.fetchone() is not None
    finally:
        cursor.close()
        conn.close()


class Devices(Resource):
    def get(self):
        api_key = request.headers.get("x-api-key")
        if not api_key or not is_valid_api_key(api_key):
            return {"error": "Unauthorized"}, 401
        
        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM network_device")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            return {"error": str(e)}, 500
        finally:
            if 'conn' in locals() and conn.open:
                cursor.close()
                conn.close()
