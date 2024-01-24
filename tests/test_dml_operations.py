import pytest

from utils.data_generator import generate_user_data


@pytest.fixture(autouse=True)
def setup_method(db_connection):
    """
    Create the 'users' table if it doesn't exist.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT
    );
    """
    db_connection.execute_query(create_table_query)


def test_insert_user(db_connection):
    """
    Test the insertion of a user into the database.
    """
    count_before_insert = db_connection.fetch_one("SELECT COUNT(*) FROM users;")
    user_data = generate_user_data()
    insert_query = """
    INSERT INTO users (id, name, age)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    db_connection.execute_query(insert_query, (user_data['id'], user_data['name'], user_data['age']))
    count_after_insert = db_connection.fetch_one("SELECT COUNT(*) FROM users;")

    assert count_after_insert > count_before_insert, "Number of rows in the table did not increase after insertion"


def test_update_user(db_connection):
    """
    Test the update operation on a user record.
    """
    new_age = 30
    update_query = """
    UPDATE users
    SET age = %s
    WHERE name = %s;
    """
    username = db_connection.fetch_one("SELECT name FROM users;")[0]
    db_connection.execute_query(update_query, (new_age, username))
    updated_age = db_connection.fetch_one(f"SELECT age FROM users WHERE name = '{username}';")[0]
    assert updated_age == new_age, "Failed to update user age"


def test_delete_user(db_connection):
    """
    Test the deletion of a user from the database.
    """
    username = db_connection.fetch_one("SELECT name FROM users;")[0]
    db_connection.execute_query(f"DELETE FROM users WHERE name = '{username}';")
    result = db_connection.fetch_one(f"SELECT * FROM users WHERE name = '{username}'")
    assert result is None, "Failed to delete user"
