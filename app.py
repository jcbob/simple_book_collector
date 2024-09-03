from utils import database


USER_CHOICE = """Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'u' to unmark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    book_name = input("Enter book name: ")
    book_author = input("Enter book author: ")
    new_book = {"name": book_name, "author": book_author, "read": False}
    database.books.append(new_book)
    return


def list_all_books():
    if database.books == []:
        print("No books in database")
        return
    print("----------------------")
    for book in database.books:
        print(f'"{book["name"]}" by {book["author"]}')
        if book["read"]:
            print("Read")
        else:
            print("Not read yet")
        print("----------------------")
    return


def prompt_read_book():
    if database.books == []:
        print("No books in database")
        return
    read_book = input("Enter the name of the book that you read: ")
    for book in database.books:
        if book["read"]:
            print("You have already read this book")
            return
        if book["name"] == read_book:
            book["read"] = True
            print(f'Congratulations on reading "{book["name"]}" by {book["author"]}!')
    return


def prompt_unread_book():
    if database.books == []:
        print("No books in database")
        return
    read_book = input("Enter the name of the book you want to 'unread': ")
    for book in database.books:
        if not book["read"]:
            print("You haven't yet read this book - you cannot mark it as unread")
            return
        if book["name"] == read_book:
            book["read"] = False
    return


def prompt_delete_book():
    if database.books == []:
        print("No books in database")
        return
    delete_book = input("Enter the name of the book that you want to delete: ")
    database.books = [b for b in database.books if b["name"] != delete_book]
    return


user_options = {
        'a': prompt_add_book,
        'l': list_all_books,
        'r': prompt_read_book,
        'u': prompt_unread_book,
        'd': prompt_delete_book
        }


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_options:
            user_options[user_input]()
        else:
            print("Invalid option, try again")
        user_input = input(": ")


menu()
