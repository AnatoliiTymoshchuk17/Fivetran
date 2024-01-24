import psycopg2
from psycopg2 import OperationalError, pool


class Database:
    def __init__(self, db_config):
        """
        Initialize the database connection using a connection pool.
        :param db_config: A dictionary containing database configuration like host, dbname, user, password.
        """
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, **db_config)
        except OperationalError as e:
            raise Exception(f"Error connecting to PostgreSQL database: {e}")

    def get_connection(self):
        """
        Get a connection from the connection pool.
        :return: a psycopg2 connection object.
        """
        return self.connection_pool.getconn()

    def release_connection(self, connection):
        """
        Release a connection back to the connection pool.
        :param connection: The connection to be released.
        """
        self.connection_pool.putconn(connection)

    def execute_query(self, query, params=None):
        """
        Execute a given SQL query with optional parameters.
        :param query: SQL query string.
        :param params: Optional parameters for the SQL query.
        """
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
        except OperationalError as e:
            connection.rollback()
            raise Exception(f"Error executing query: {e}")
        finally:
            self.release_connection(connection)

    def fetch_all(self, query, params=None):
        """
        Fetch all rows from the result of a query.
        :param query: SQL query string.
        :param params: Optional parameters for the SQL query.
        :return: List of rows returned by the query.
        """
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except OperationalError as e:
            raise Exception(f"Error fetching data: {e}")
        finally:
            self.release_connection(connection)

    def fetch_one(self, query, params=None):
        """
        Fetch the first row from the result of a query.
        :param query: SQL query string.
        :param params: Optional parameters for the SQL query.
        :return: The first row returned by the query.
        """
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            return result
        except OperationalError as e:
            raise Exception(f"Error fetching data: {e}")
        finally:
            self.release_connection(connection)

    def close_connection(self):
        """
        Closes all database connections in the pool.
        """
        self.connection_pool.closeall()
