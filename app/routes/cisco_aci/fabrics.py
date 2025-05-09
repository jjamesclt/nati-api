from flask import jsonify
from flask_restful import Resource
from app.units.cisco_aci import get_fabrics, get_nodes

class Fabrics(Resource):
    def get(self):
        try:
            fabrics = get_fabrics()
            return jsonify(fabrics)
        except Exception as e:
            return {"error": str(e)}, 500


class Nodes(Resource):
    def get(self):
        try:
            nodes = get_nodes()
            return jsonify(nodes)
        except Exception as e:
            return {"error": str(e)}, 500
