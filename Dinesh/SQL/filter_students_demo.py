import sqlite3

try:
    connection=sqlite3.connect("dinesh_db.sqlite3")
    cursor=connection.cursor()
    filter_query="SELECT title,author, price FROM book where title =? "
    filter_value=("gg")
    cursor.execute(filter_query,filter_value)
    results=cursor.fetchall()
    for row in results:
        print(row)
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()

