# from datetime import datetime, timedelta
from save_all_books import save_lend_books, save_all_books


def return_book(all_books, lend_books):
    title = input("Enter the book title to return: ")
    borrower_name = input("Enter the borrower's name: ")

    lend_found = False

    for entry in lend_books:
        if entry["book_title"].lower() == title.lower() and entry["borrower_name"].lower() == borrower_name.lower():
            lend_found = True
            lend_books.remove(entry)

            for book in all_books:
                if book["title"].lower() == title.lower():
                    book["quantity"] += 1
                    break

            save_lend_books(lend_books)
            save_all_books(all_books)
            print(f"Book '{title}' successfully returned by {borrower_name}.")
            break

    if not lend_found:
        print("Lending record not found.")