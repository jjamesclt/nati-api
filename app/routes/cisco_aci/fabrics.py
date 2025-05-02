from flask import jsonify
from flask_restful import Resource
from app.units.cisco_aci import get_fabrics

class Fabrics(Resource):
    def get(self):
        try:
            fabrics = get_fabrics()
            return jsonify(fabrics)
        except Exception as e:
            return {"error": str(e)}, 500
