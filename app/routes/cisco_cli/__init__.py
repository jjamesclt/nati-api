from flask import Blueprint
from flask_restful import Api

#from .fabrics import Fabrics  # ← Adjust for actual resource files

# Define the blueprint
cisco_cli_bp = Blueprint('cisco_cli', __name__, url_prefix='/api/cisco-cli')
api = Api(cisco_cli_bp)

# Register your RESTful endpoints
#api.add_resource(Fabrics, '/fabrics')
