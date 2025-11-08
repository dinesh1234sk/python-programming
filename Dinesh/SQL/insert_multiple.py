import sqlite3

try:
    connection=sqlite3.connect("dinesh2_db.sqbpro")
    cursor=connection.cursor()
    insert_data_query="""
        INSERT INTO book(title,author,price) VALUES (?,?,?)
        """
    book_records = [
        ("hh","jj",887),
        ("gg","kk",776),
        ("dd","ll",453)
         ]
    cursor.executemany(insert_data_query,book_records)
    connection.commit()
    print("Successfully inserted data")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
