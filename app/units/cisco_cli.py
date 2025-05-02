import pymysql
from flask import jsonify
#from config import db_config  # Assuming this exists and works
from app.utils.db import get_db_connection  # or wherever you store the helper
