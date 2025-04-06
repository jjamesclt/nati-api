# app/db_test.py

import pymysql
import configparser
import os

def test_db_connection():
    try:
        # Load the config from the root folder
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'nati.ini')
        config = configparser.ConfigParser()
        config.read(config_path)

        db_config = {
            'host': config['database']['host'],
            'port': int(config['database']['port']),
            'user': config['database']['username'],
            'password': config['database']['password'],
            'database': config['database']['database']
        }

        # Attempt to connect
        connection = pymysql.connect(**db_config)
        print("Database connection successful!")

        return True

    except pymysql.err.OperationalError as e:
        print(f"Operational error: {e}")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

# Optional: Run as script
if __name__ == '__main__':
    test_db_connection()
