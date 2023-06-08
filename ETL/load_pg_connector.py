""" Make connection to PG"""
import os
import psycopg2
from dotenv import load_dotenv

class PGConn:

    """
    Class to make initial connection to PostgreSQL 
    """
    # Load env file
    load_dotenv()

    _PG_USER = os.environ.get('PG_USER')
    _PG_DB = os.environ.get('PG_DB')
    _PG_PW = os.environ.get('PG_PW')
    _PG_PORT = os.environ.get('PG_PORT')

    def __init__(self):
        self._db = self.connect()
        self._cursor = self._db.cursor()

    def connect(self):
        """
        Method to make a connection Object
        """
        try:
            return psycopg2.connect(
                database = self._PG_DB,
                user = self._PG_USER,
                password = self._PG_PW,
                host = 'localhost',
                port = self._PG_PORT
            )
        except Exception (psycopg2.Error) as error:
            print(f"Error Occured while creating connection!, {error}")
