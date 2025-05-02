from flask import Blueprint
from flask_restful import Api

from .fabrics import Fabrics  # ← Adjust for actual resource files

# Define the blueprint
cisco_aci_bp = Blueprint('cisco_aci', __name__, url_prefix='/api/cisco-aci')
api = Api(cisco_aci_bp)

# Register your RESTful endpoints
api.add_resource(Fabrics, '/fabrics')
