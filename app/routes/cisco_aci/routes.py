from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import pymysql
import configparser

# Blueprint setup
aci_bp = Blueprint('cisco_aci', __name__, url_prefix='/api/cisco_aci')
api = Api(aci_bp)

# Load DB credentials from nati.ini
config = configparser.ConfigParser()
config.read('nati.ini')

db_config = {
    'host': config['database']['host'],
    'port': int(config['database']['port']),
    'user': config['database']['username'],
    'password': config['database']['password'],
    'database': config['database']['database']
}

class Fabrics(Resource):
    def get(self):
        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM aci_fabric")
            fabrics = cursor.fetchall()
            return jsonify(fabrics)
        except Exception as e:
            return {"error": str(e)}, 500
        finally:
            if 'conn' in locals() and conn.open:
                cursor.close()
                conn.close()

# Register the resource route
api.add_resource(Fabrics, '/fabrics')
