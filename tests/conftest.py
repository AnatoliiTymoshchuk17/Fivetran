import pytest
from utils import Database


@pytest.fixture(scope="module")
def db_connection():
    """
    Creates a database connection for the duration of the module.
    """
    db_config = {
        "host": "localhost",
        "port": "5432",
        "user": "postgres",
        "password": "postgres",
        "dbname": "bot_db"
    }
    db = Database(db_config)
    yield db
    db.close_connection()


@pytest.fixture(scope="session")
def setup_database(db_connection):
    """
    Sets up the database state before tests run. This could include
    creating tables, inserting initial data, etc.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS your_table (
        id SERIAL PRIMARY KEY,
        column1 VARCHAR(255),
        column2 INTEGER
    );
    """
    db_connection.execute_query(create_table_query)
    yield

    drop_table_query = "DROP TABLE IF EXISTS your_table;"
    db_connection.execute_query(drop_table_query)
