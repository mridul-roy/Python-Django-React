import json

def view_all_books(all_books):
    with open("all_books.json","r") as file:
        json.load(file)
        if all_books != []:
            for id, book in enumerate(all_books,start=1):
                print(f"{id}. Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | "
                  f"Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book added at: {book['addedTime']} | Last updated: {book['last_updatedTime']}")
        else:
            print("No books found in the system.")