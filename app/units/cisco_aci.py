import pymysql
from flask import jsonify
#from config import db_config  # Assuming this exists and works
from app.utils.db import get_db_connection  # or wherever you store the helper


def get_fabrics():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_fabric")
        fabrics = cursor.fetchall()
        return fabrics
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()
