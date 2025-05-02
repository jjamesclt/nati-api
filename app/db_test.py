# app/db_test.py

from nati.config_manager import ConfigManager
import pymysql
import os

def test_db_connection():
    try:
        # Load the config from the root folder
        config = ConfigManager()

        db_config = {
            'host': config.get('database.host'),
            'port': int(config.get('database.port')),
            'user': config.get('database.username'),
            'password': config.get('database.password'),
            'database': config.get('database.database'),
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
