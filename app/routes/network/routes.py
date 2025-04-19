from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import pymysql
import configparser

# Blueprint setup
network_bp = Blueprint('network', __name__, url_prefix='/api/network')
api = Api(network_bp)

# Load DB credentials
config = configparser.ConfigParser()
config.read('nati.ini')

db_config = {
    'host': config['database']['host'],
    'port': int(config['database']['port']),
    'user': config['database']['username'],
    'password': config['database']['password'],
    'database': config['database']['database']
}

class Devices(Resource):
    def get(self):
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

# Register route
api.add_resource(Devices, '/devices')
