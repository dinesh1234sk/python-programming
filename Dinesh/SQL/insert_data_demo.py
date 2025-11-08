import sqlite3

try:
    connection = sqlite3.connect("dinesh2_db.sqbpro")
    cursor = connection.cursor()
    insert_data_query = """
         INSERT INTO book(title,author,price) VALUES (?,?,?)
         """
    book_data=("life of pi","dinesh",550)
    cursor.execute(insert_data_query, book_data)
    connection.commit()
    print("student data inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
