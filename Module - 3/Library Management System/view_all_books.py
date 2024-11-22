def view_all_books(all_books):
    if all_books:
        print("\nList of Books:")
        for idx, book in enumerate(all_books, 1):
            print(f"{idx}. Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | "
                  f"Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
    else:
        print("No books found in the system.")
