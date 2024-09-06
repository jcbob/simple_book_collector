import sqlite3
"""
Concerned with storing and retrieving books from a json file
Format of json file:
[
  {"name": name1, "author": author1, "read": read1},
  {"name": name2, "author": author2, "read": read2}
]
"""

books_file = 'books.json'


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
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def list_books():
    print("----------------------")
    with open('books.json', 'r') as file:
        books = json.load(file)
        for book in books:
            read = "YES" if book["read"] else "NO"
            print(f'"{book["name"]}" by {book["author"]}\n Read: {read}')
            print("----------------------")


def is_empty():
    books = get_books()
    if books == []:
        return True
    else:
        return False


def mark_book_as_read(name):
    books = get_books()
    for book in books:
        if book["name"] == name:
            if book["read"]:
                print("You have already read this book")
                return
            book["read"] = True
            print(f'Congratulations on reading "{book["name"]}" by {book["author"]}!')
    _save_all_books(books)


def mark_book_as_unread(name):
    books = get_books()
    for book in books:
        if book["name"] == name:
            if not book["read"]:
                print("You haven't yet read this book - you cannot mark it as unread")
                return
            book["read"] = False
            print(f'Successfully unread "{book["name"]}" by {book["author"]}')
    _save_all_books(books)


def has_book(book_to_check):
    books = get_books()
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(name):
    books = get_books()
    books = [book for book in books if book["name"] != name]
    print("Successfully deleted the book!")
    _save_all_books(books)


if __name__ == "__main__":
    create_book_table()
    add_book("dun", "don")
    add_book("bum", "bom")
    add_book("hub", "dub")
    list_books()
