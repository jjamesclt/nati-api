from .network import network_bp
from .cisco_aci import cisco_aci_bp
from .db_check import db_check_bp

def register_blueprints(app):
    app.register_blueprint(network_bp)
    app.register_blueprint(cisco_aci_bp)
    app.register_blueprint(db_check_bp)
