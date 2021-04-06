import psycopg2
import json

class Database:

    def __init__(self):
        file = open('C:/CODING/GIT/InternTracker/InternTracker/Database/connection.config')
        credentials_raw = file.read()
        credentials_dict = json.loads(credentials_raw)

        self.__dbname = str(credentials_dict["dbname"])
        self.__user = str(credentials_dict["user"])
        self.__password = str(credentials_dict["password"])

    def connect(self):
        connection = psycopg2.connect(f"dbname = {self.__dbname} user = {self.__user} password = {self.__password}")
        return connection

obj = Database()