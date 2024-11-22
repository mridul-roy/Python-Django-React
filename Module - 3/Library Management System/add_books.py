from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter the name of the Book: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN number: ")
    year = input("Enter the published year: ")
    price = input("Enter the price: ")
    quantity = input("Enter the quantity: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }
    
    all_books.append(book)
    save_all_books(all_books)

    print("Book added successfully.")

    return all_books
