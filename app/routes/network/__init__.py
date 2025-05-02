from flask import Blueprint
from flask_restful import Api
from .devices import Devices
from .mac_lookup import MacLookup

network_bp = Blueprint('network', __name__, url_prefix='/api/network')
api = Api(network_bp)

api.add_resource(Devices, '/devices')
api.add_resource(MacLookup, '/mac-lookup/<string:mac_addr>')
