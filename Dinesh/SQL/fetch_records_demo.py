import sqlite3

try:
    connection = sqlite3.connect("dinesh2_db.sqbpro")
    cursor = connection.cursor()
    select_all_query="SELECT title, author,price FROM book"
    cursor.execute(select_all_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    select_titles_query="SELECT title FROM book"
    cursor.execute(select_titles_query)
    titles = cursor.fetchall()
    for title in titles:
        print(title)
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()

