import sqlite3
from sqlite3 import Error


def connection():
    #  Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(r"./data/todolist_python.db")
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    #  Create a table from the SQLite3 database
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"./data/todolist_python.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    task text NOT NULL,
                                    status text NOT NULL,
                                    user_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    conn = connection()
