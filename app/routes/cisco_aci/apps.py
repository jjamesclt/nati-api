from flask import jsonify
from flask_restful import Resource
from app.units.cisco_aci import get_epgs, get_aps, get_bds

class EPGs(Resource):
    def get(self):
        try:
            epgs = get_epgs()
            return jsonify(epgs)
        except Exception as e:
            return {"error": str(e)}, 500


class APs(Resource):
    def get(self):
        try:
            aps = get_aps()
            return jsonify(aps)
        except Exception as e:
            return {"error": str(e)}, 500

class BDs(Resource):
    def get(self):
        try:
            bds = get_bds()
            return jsonify(bds)
        except Exception as e:
            return {"error": str(e)}, 500
