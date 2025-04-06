"""
NATI API - Network Analytics and Telemetry Interface API
"""

from flask import Flask, redirect
from flask_restful import Resource, Api, reqparse

# Initialize Flask
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True

# RESTful API setup
api = Api(app)

# Optional welcome route
@app.route('/')
def hello():
    return "Hello World - Welcome to NATI API!"

# Header parser for APIs
key_parser = reqparse.RequestParser()
key_parser.add_argument("x-api-key",
                        type=str,
                        required=True,
                        help="API Key is required",
                        location='headers')

# ✅ Import and register your new Blueprint
from app.routes.db_check import db_check_bp
app.register_blueprint(db_check_bp)

# Flask app runner
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
