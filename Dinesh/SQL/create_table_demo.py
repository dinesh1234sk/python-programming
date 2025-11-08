import sqlite3


try:
    connection=sqlite3.connect("dinesh2_db.sqbpro")
    cursor=connection.cursor()
    create_table_query = """
         CREATE TABLE book (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title VARCHAR(30),
         author VARCHAR(40),
         PRICE DECIMAL(10,2))
         """
    cursor.execute(create_table_query)
    connectin.commit();
    print("Table created successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()