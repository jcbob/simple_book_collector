"""
Concerned wiht storing and retrieving books from a list
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


def has_book(book_to_check):
    for book in books:
        if book["name"] == book_to_check:
            return True
    return False


def delete_book(book_to_delete):
    for book in books:
        if book_to_delete == book["name"]:
            books.remove(book)
            break


if __name__ == "__main__":
    add_book("dun", "dun")
    print(books)

    delete_book("dun")
    print(books)
