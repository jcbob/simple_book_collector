import sqlite3
"""
Concerned with storing and retrieving books from a database
"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


def get_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]

    connection.close()
    return books


def is_empty():
    books = get_books()
    if books == []:
        return True
    else:
        return False


def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))
    connection.commit()
    connection.close()


def mark_book_as_unread(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET read=0 WHERE name=?", (name,))
    connection.commit()
    connection.close()


def has_book(book_to_check):
    books = get_books()
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE name=?", (name,))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_book_table()
    add_book("dun", "don")
    add_book("bum", "bom")
    add_book("hub", "dub")
    list_books()
