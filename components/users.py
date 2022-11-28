from data.db_config import connection
import hashlib


def hash_password(password):
    """ Hash a password for storing. """
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password):
    """ Create a new user """
    if select_username(username):
        print("Username already exists")
    else:
        conn = connection()
        sql = ''' INSERT INTO users(username, password)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (username.lower(), hash_password(password)))
        conn.commit()
        return cur.lastrowid


def check_user(username, password):
    """ Search for a user """
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))

    rows = cur.fetchall()
    print(username + " " + password)

    if len(rows) == 1:
        print("true")
        return True
    else:
        print("false")
        return False


def select_username(username):
    """ Search for a username """
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE username == ?", (username,))
    #  print(username)

    rows = cur.fetchall()

    if len(rows) == 1:
        print("true")
        return True
    else:
        print("false")
        return False
