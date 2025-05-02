import pymysql
from flask import jsonify
from app.utils.db import get_db_connection


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


def get_nodes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_node")
        nodes = cursor.fetchall()
        return nodes
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()


def get_tenants():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_tenant")
        tenants = cursor.fetchall()
        return tenants
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()


def get_vrfs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_vrf")
        vrfs = cursor.fetchall()
        return vrfs
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()



def get_epgs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_epg")
        epgs = cursor.fetchall()
        return epgs
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()

def get_aps():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_ap")
        aps = cursor.fetchall()
        return aps
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()

def get_bds():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aci_bd")
        bds = cursor.fetchall()
        return bds
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if 'conn' in locals() and conn.open:
            cursor.close()
            conn.close()
