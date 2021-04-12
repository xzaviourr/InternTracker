import psycopg2
import json
from Logger.logger import db_logger

class Database:

    def __init__(self):
        try:
            file = open('Database/connection.config')
            credentials_raw = file.read()
            credentials_dict = json.loads(credentials_raw)
        except:
            db_logger.error('Credentials file cannot be opened')

        self.__dbname = str(credentials_dict["dbname"])
        self.__user = str(credentials_dict["user"])
        self.__password = str(credentials_dict["password"])
        self.__host = str(credentials_dict["host"])

    def connect(self):
        try:
            connection = psycopg2.connect(dbname = str(self.__dbname), user = str(self.__user), password = str(self.__password), host = str(self.__host))
            return connection
        except:
            db_logger.error("Connecting database failed")
