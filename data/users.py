from data.db_config import connection


def create_user(username, password):
    """ Create a new user """
    conn = connection()
    sql = ''' INSERT INTO users(username, password)
                VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (username.lower(), password))
    conn.commit()
    return cur.lastrowid


def select_user(username, password):
    """ Search for a user """
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    rows = cur.fetchall()

    if len(rows) == 1:
        print("true")
    else:
        print("false")


def select_username(username):
    """ Search for a username """
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE username == ?", username)

    rows = cur.fetchall()

    if len(rows) == 1:
        print("true")
    else:
        print("false")
