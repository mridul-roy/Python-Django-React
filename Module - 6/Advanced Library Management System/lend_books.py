# from save_all_books import save_lend_books

# def lend_books_form(lend_books):
#     print("Lend Books Form!!!\n")
#     borrower_name = input("Enter your name: ")
#     phone_number = input("Enter phone number: ")
#     book_title = input("Enter the book name: ")
#     return_date = input("Enter return date(YY-MM-DD): ")
    
#     l_book ={
#         "borrower_name": borrower_name,
#         "phone_number": phone_number,
#         "book_title": book_title,
#         "return_date": return_date
#     }
    
#     lend_books.append(l_book)
#     save_lend_books(lend_books)
    
#     print("Borrower info saved successful.")
#     return lend_books

from datetime import datetime, timedelta
from save_all_books import save_lend_books, save_all_books
import json

def lend_books_form(all_books, lend_books):
    title = input("Enter the book title to lend: ")
    book_found = False

    for book in all_books:
        if book["title"].lower() == title.lower() and book["quantity"] > 0:
            book_found = True
            borrower_name = input("Enter borrower's name: ")
            phone_number = input("Enter borrower's phone number: ")
            due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

            lend_entry = {
                "borrower_name": borrower_name,
                "phone_number": phone_number,
                "book_title": book["title"],
                "due_date": due_date
            }

            lend_books.append(lend_entry)
            book["quantity"] -= 1
            save_lend_books(lend_books)
            save_all_books(all_books)

            print(f"Book '{book['title']}' lent successfully! Due date: {due_date}")
            break

    if not book_found:
        print("Book not available for lending or title not found.")

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
