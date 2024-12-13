from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter the name of the Book: ")
    author = input("Enter the author's name: ")
    while True:
        try:
            year = int(input("Enter the published year: "))
            break
        except ValueError:
            print("Invalid input.Year must be positive integer.")
            
    while True:
        try: 
            price = int(input("Enter the price: "))
            break
        except ValueError:
            print("Invalide input. Price must be positive integer")
            
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            print("Invalid input.Quantity must be positive integer.")
    
    isbn = random.randint(10000,99999)
    addedTime = datetime.now().strftime("%d-%m-%Y,%H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "addedTime": addedTime,
        "last_updatedTime": ""
    }
    
    all_books.append(book)
    save_all_books(all_books)

    print("Book added successfully.")

    return all_books
