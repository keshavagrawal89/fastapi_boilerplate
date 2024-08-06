import psycopg2
from psycopg2 import pool
from app.core.config import settings

DATABASE_URL = settings.database_url

class Database:
    def __init__(self):
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20, DATABASE_URL
        )

    def get_connection(self):
        if self.connection_pool:
            return self.connection_pool.getconn()

    def release_connection(self, conn):
        if self.connection_pool:
            self.connection_pool.putconn(conn)

    def close_all_connections(self):
        if self.connection_pool:
            self.connection_pool.closeall()

database = Database()
