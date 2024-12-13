from datetime import datetime
from save_all_books import save_all_books

def update_books(all_books):
    search_book = input("Enter the Title of the book: ")
    
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter the name of the Book: ").strip()
            author = input("Enter the author's name: ").strip()
            year = input("Enter the published year: ").strip()
            price = input("Enter the price: ").strip()
            quantity = input("Enter the quantity: ").strip()
            
            last_updatedTime = datetime.now().strftime("%d-%m-%Y,%H:%M:%S")
            
            # Only update if the user enters a new value
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if year:
                book["year"] = int(year)
            if price:
                book["price"] = int(price)
            if quantity:
                book["quantity"] = int(quantity)
            book["last_updatedTime"] = last_updatedTime
            
            save_all_books(all_books)
            print("Book updated successfully.")
            return all_books
            
    else:
        print(f"{search_book} book is not available.")
