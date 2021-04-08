import psycopg2
import json
from Logger.logger import db_logger

class Database:

    def __init__(self):
        try:
            file = open('InternTracker/Database/connection.config')
            credentials_raw = file.read()
            credentials_dict = json.loads(credentials_raw)
        except:
            db_logger.error('Credentials file cannot be opened')

        self.__dbname = str(credentials_dict["dbname"])
        self.__user = str(credentials_dict["user"])
        self.__password = str(credentials_dict["password"])

    def connect(self):
        try:
            connection = psycopg2.connect(f"dbname = {self.__dbname} user = {self.__user} password = {self.__password}")
        except:
            db_logger.error("Connecting database failed")
        return connection
