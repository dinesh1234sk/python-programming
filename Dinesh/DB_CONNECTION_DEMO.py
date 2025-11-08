import sqlite3
try:
    connection=sqlite3.connect('dinesh2_db.db')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM books")
    print("books in database")
    for row in cursor.fetchall():
       print(row)
except sqlite3.Error as e:
    print(f"SQlite error:{e}")
finally:
    if connection:
        connection.close()
