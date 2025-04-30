from flask_restful import Resource
from flask import jsonify
import re
from app.routes.network.db import get_db_connection

class MacLookup(Resource):
    def get(self, mac_addr):
        try:
            oui = self.normalize_mac(mac_addr)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM network_ouidb WHERE oui = %s", (oui,))
            row = cursor.fetchone()

            if row:
                keys = [desc[0] for desc in cursor.description]
                result = dict(zip(keys, row))
            else:
                result = {'message': f'OUI {oui} not found'}

            cursor.close()
            conn.close()
            return result

        except Exception as e:
            return {'error': str(e)}, 500

    def normalize_mac(self, mac):
        cleaned = re.sub(r'[^0-9A-Fa-f]', '', mac)
        return cleaned.upper()[0:6]
