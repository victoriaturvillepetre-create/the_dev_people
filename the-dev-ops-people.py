import sqlite3

sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL, 
            year_group INT,
            GitHub_user_name TEXT
        );"""
]

insert_sql = '''INSERT INTO people(first_name, last_name, year_group, GitHub_user_name)
             VALUES("Simon", "Holland", '10', 'inyoka') '''
#Blame Martin

try:
    with sqlite3.connect('DEVOPS_PEOPLE') as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully."); cursor = conn.cursor()
        for statement in sql_statements: cursor.execute(statement)
        print("Tables created successfully.")

        cursor.execute(insert_sql)
        conn.commit()
        cursor.execute('select * from people')
        rows = cursor.fetchall()
        print(rows)

except sqlite3.OperationalError as e:
    print(f'Error:  {e}')