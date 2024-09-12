from typing import List, Dict
from typing import Union

from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database
"""


Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    return books


def is_empty() -> bool:
    books = get_books()
    if books == []:
        return True
    else:
        return False


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))


def mark_book_as_unread(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=0 WHERE name=?", (name,))


def has_book(book_to_check: str) -> bool:
    books = get_books()
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=?", (name,))


if __name__ == "__main__":
    create_book_table()
    add_book("dun", "don")
    add_book("bum", "bom")
    add_book("hub", "dub")
