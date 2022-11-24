import sqlite3
from sqlite3 import Error


def connection():
    #  Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(r"./data/todolist_python.db")
        #  print(sqlite3.version)
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


def create_main_tables():
    database = r"./data/todolist_python.db"

    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    username text NOT NULL UNIQUE,
                                    password text NOT NULL
                            ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    user integer NOT NULL,
                                    title text NOT NULL,
                                    description text NOT NULL,
                                    priority integer NOT NULL,
                                    due_date text NOT NULL,
                                    FOREIGN KEY (priority) REFERENCES priorities(id),
                                    FOREIGN KEY (user) REFERENCES users(id)
                            );"""

    sql_create_priorities_table = """CREATE TABLE IF NOT EXISTS priorities (
                                    id integer PRIMARY KEY,
                                    priority text NOT NULL
                                );"""

    conn = connection()

    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
        # create priorities table
        create_table(conn, sql_create_priorities_table)
        print("Database created successfully")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    create_main_tables()
