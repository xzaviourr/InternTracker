import psycopg2
import json
import os
# from Logger.logger import db_logger
from dotenv import load_dotenv

load_dotenv()

class Database:

    def __init__(self):
        try:
            file = open('Database/connection.config')
            credentials_raw = file.read()
            credentials_dict = json.loads(credentials_raw)
        except:
            # db_logger.error('Credentials file cannot be opened')
            print('INVALID CREDENTIALS IN CONFIG')

        self.__dbname = str(os.getenv('DB_NAME'))
        self.__user = str(os.getenv('DB_USER'))
        self.__password = str(os.getenv('DB_PASSWORD'))
        self.__host = str(os.getenv('DB_HOST'))

    def connect(self):
        try:
            connection = psycopg2.connect(dbname = str(self.__dbname), user = str(self.__user), password = str(self.__password), host = str(self.__host))
            return connection
        except:
            # db_logger.error("Connecting database failed")
            print("ERROR CONNECTING TO DATABASE")
