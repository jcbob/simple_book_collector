import json
"""
Concerned with storing and retrieving books from a json file
Format of json file:
[
  {"name": name1, "author": author1, "read": read1},
  {"name": name2, "author": author2, "read": read2}
]
"""

books_file = 'books.json'


def create_book_storage():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_books()
    books.append({"name": name, "author": author, "read": False})
    _save_all_books(books)


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
        print(type(books))
        for book in books:

            read = "YES" if book["read"] else "NO"
            print(f'"{book["name"]}" by {book["author"]}\n Read: {read}')
            print("----------------------")


def is_empty():
    if books == []:
        return True
    else:
        return False




def mark_book_as_read(name):
    for book in books:
        if book["read"]:
            print("You have already read this book")
            return

        if book["name"] == name:
            book["read"] = True
            print(f'Congratulations on reading "{book["name"]}" by {book["author"]}!')


def mark_book_as_unread(name):
    for book in books:
        if not book["read"]:
            print("You haven't yet read this book - you cannot mark it as unread")
            return

        if book["name"] == name:
            book["read"] = False
            print(f'Successfully unread "{book["name"]}" by {book["author"]}')


def has_book(book_to_check):
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(name):
    global books
    books = [book for book in books if book["name"] != name]
    print("Successfully deleted the book!")


if __name__ == "__main__":
    create_book_storage()
    add_book("dun", "don")
    add_book("bum", "bom")
    add_book("hub", "dub")
