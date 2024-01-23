import pytest
from utils import generate_user_data


def test_insert_user(db_connection):
    """
    Test the insertion of a user into the database.
    """
    user_data = generate_user_data()
    insert_query = """
    INSERT INTO users (username, age, join_date)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    user_id = db_connection.execute_query(insert_query,
                                          (user_data['username'], user_data['age'], user_data['join_date']))
    assert user_id is not None, "Failed to insert user data"


def test_update_user(db_connection):
    """
    Test the update operation on a user record.
    """
    new_age = 30
    update_query = """
    UPDATE users
    SET age = %s
    WHERE username = %s;
    """
    db_connection.execute_query(update_query, (new_age, "existing_username"))
    select_query = "SELECT age FROM users WHERE username = %s;"
    updated_age = db_connection.fetch_one(select_query, ("existing_username",))
    assert updated_age == new_age, "Failed to update user age"


def test_delete_user(db_connection):
    """
    Test the deletion of a user from the database.
    """
    delete_query = "DELETE FROM users WHERE username = %s;"
    db_connection.execute_query(delete_query, ("username_to_delete",))
    select_query = "SELECT * FROM users WHERE username = %s;"
    result = db_connection.fetch_one(select_query, ("username_to_delete",))
    assert result is None, "Failed to delete user"
