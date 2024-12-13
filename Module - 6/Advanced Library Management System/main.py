import add_books
import save_all_books
import view_all_books
from restore_all_books import restore_all_books
import update_books
import remove_books
from lend_books import lend_books_form
from return_books import return_book

all_books = []
lend_books = []

while True:
    print("\nWelcome to Library Management System!!!")
    print("1. Add Books: ")
    print("2. View all Books: ")
    print("3. Update Books: ")
    print("4. Remove Books: ")
    print("5. Lend book: ")
    print("6. Return book: ")
    print("0. Exit")

    all_books = restore_all_books(all_books)

    option = input("Enter an Option: ")

    if option == "0":
        print("Thank you.")
        break
    elif option == "1":
        all_books = add_books.add_books(all_books)
    elif option == "2":
        view_all_books.view_all_books(all_books)
    elif option == "3":
        update_books.update_books(all_books)
    elif option == "4":
        remove_books.remove_books(all_books)
    elif option == "5":
        lend_books_form(all_books, lend_books)
    elif option == "6":
        return_book(all_books, lend_books)
    else:
        print("Invalid choice!")
