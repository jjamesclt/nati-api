from flask import Blueprint
from flask_restful import Api

from .fabrics import Fabrics, Nodes
from .tenants import Tenants, VRFs
from .apps import EPGs, APs, BDs

# Define the blueprint
cisco_aci_bp = Blueprint('cisco_aci', __name__, url_prefix='/api/cisco-aci')
api = Api(cisco_aci_bp)

# Register your RESTful endpoints
api.add_resource(Fabrics, '/fabrics')
api.add_resource(Nodes, '/nodes')
api.add_resource(Tenants, '/tenants')
api.add_resource(VRFs, '/vrfs')
api.add_resource(EPGs, '/epgs')
api.add_resource(APs, '/aps')
api.add_resource(BDs, '/bds')
