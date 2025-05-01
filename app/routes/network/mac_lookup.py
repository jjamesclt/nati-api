from flask_restful import Resource
import re
from app.utils.db import get_db_connection  # or wherever you store the helper

class MacLookup(Resource):
    def get(self, mac_addr):
        try:
            oui = self.normalize_mac(mac_addr)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT vendor_name FROM network_ouidb WHERE mac_prefix = %s", (oui,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()

            if row:
                keys = [desc[0] for desc in cursor.description]
                return dict(zip(keys, row))
            else:
                return {'message': f'OUI {oui} not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500

    def normalize_mac(self, mac):
        return re.sub(r'[^0-9A-Fa-f]', '', mac).upper()[0:6]
