def test_create_table(db_connection):
    """
    Test the creation of a new table in the database.
    """
    create_table_query = """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
    """
    db_connection.execute_query(create_table_query)

    table_check_query = "SELECT to_regclass('public.users');"
    table_exists = db_connection.fetch_one(table_check_query)[0]
    assert table_exists == 'users', "Table was not created successfully"


def test_alter_table(db_connection):
    """
    Test altering an existing table in the database.
    """
    alter_table_query = "ALTER TABLE users ADD COLUMN email VARCHAR(255);"
    db_connection.execute_query(alter_table_query)

    column_check_query = ("SELECT column_name FROM information_schema.columns WHERE table_name = 'users' AND "
                          "column_name = 'email';")
    column_exists = db_connection.fetch_one(column_check_query)[0]
    assert column_exists == 'email', "Column 'name' was not added successfully"


def test_drop_table(db_connection):
    """
    Test the deletion (dropping) of a table in the database.
    """
    drop_table_query = "DROP TABLE IF EXISTS users;"
    db_connection.execute_query(drop_table_query)

    table_check_query = "SELECT to_regclass('public.users');"
    table_exists = db_connection.fetch_one(table_check_query)[0]
    assert table_exists is None, "Table was not dropped successfully"
