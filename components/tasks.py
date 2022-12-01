from data.db_config import connection


def create_task(task):
    """ Create a new task """
    conn = connection()
    sql = ''' INSERT INTO tasks(user, title, description, priority, due_date)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def select_all_tasks(user):
    """ Query all rows in the tasks table """
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE user = ?", (user,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
