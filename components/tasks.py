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


def main():
    #  Create a new task
    with connection():

        task = (1, 'Test', 'This is a test', 1, '2023-01-01')

        create_task(task)
        print("Task created successfully: ", task)


if __name__ == '__main__':
    main()
