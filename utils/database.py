from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database
"""


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    return books


def is_empty():
    books = get_books()
    if books == []:
        return True
    else:
        return False


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))


def mark_book_as_unread(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=0 WHERE name=?", (name,))


def has_book(book_to_check):
    books = get_books()
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=?", (name,))


if __name__ == "__main__":
    create_book_table()
    add_book("dun", "don")
    add_book("bum", "bom")
    add_book("hub", "dub")
