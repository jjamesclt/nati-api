from flask import jsonify
from flask_restful import Resource
from app.units.cisco_aci import get_tenants, get_vrfs

class Tenants(Resource):
    def get(self):
        try:
            tenants = get_tenants()
            return jsonify(tenants)
        except Exception as e:
            return {"error": str(e)}, 500


class VRFs(Resource):
    def get(self):
        try:
            vrfs = get_vrfs()
            return jsonify(vrfs)
        except Exception as e:
            return {"error": str(e)}, 500
