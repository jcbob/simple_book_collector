"""
Concerned with storing and retrieving books from a list
"""

books = []


def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})


def is_empty():
    if books == []:
        return True
    else:
        return False


def get_books():
    return books


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
    add_book("dun", "dun")
    print(books)

    delete_book("dun")
    print(books)
