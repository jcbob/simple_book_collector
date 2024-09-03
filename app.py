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
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    database.add_book(name, author)
    return


def list_all_books():
    if database.is_empty():
        print("No books in database")
        return

    print("----------------------")
    for book in database.get_books():
        read = "YES" if book["read"] else "NO"
        print(f'"{book["name"]}" by {book["author"]}\n Read: {read}')
        print("----------------------")
    return


def prompt_read_book():
    if database.is_empty():
        print("No books in database")
        return

    read_book = input("Enter the name of the book that you read: ")
    if not database.has_book(read_book):
        print("There is no such book in the database")
        return

    database.mark_book_as_read(read_book)
    return


def prompt_unread_book():
    if database.is_empty():
        print("No books in database")
        return

    unread_book = input("Enter the name of the book you want to 'unread': ")
    if not database.has_book(unread_book):
        print("There is no such book in the database")
        return

    database.mark_book_as_unread(unread_book)
    return


def prompt_delete_book():
    if database.is_empty():
        print("No books in database")
        return

    delete_book = input("Enter the name of the book that you want to delete: ")
    if not database.has_book(delete_book):
        print("There is no such book in the database")
        return

    database.delete_book(delete_book)
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
