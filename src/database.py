import sqlite3
from sqlite3 import Error


def connect(path):
    """ Creates connection with given database path.
     If no db present, db is created

    :param path: Path to database
    :return: connection object
    """
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(f"Error: '{e}'")
    return conn


def execute_query(conn, query):
    """ Executes given SQL query.

    :param conn: db connection
    :param query: SQL statement
    :return: result of SQL query on database
    """
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: '{e}'")


def execute_read_query(conn, query):
    """ For SELECT queries.

    :param conn: db connection
    :param query: SQL statement
    :return: result of SQL query on database
    """
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"Error: '{e}'")
    return result

# TODO: add utility functions for extracting specific data from read_query (rather than tuples/lists)
# TODO: prevent SQL injection attacks