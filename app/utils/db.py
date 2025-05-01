# app/utils/db.py
import pymysql
from nati.config_manager import ConfigManager

config = ConfigManager()

def get_db_connection():
    return pymysql.connect(
        host=config.get("database.host"),
        port=int(config.get("database.port")),
        user=config.get("database.username"),
        password=config.get("database.password"),
        database=config.get("database.database")
    )
