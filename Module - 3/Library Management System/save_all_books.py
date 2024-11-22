def save_all_books(all_books):
    with open("ALL_BOOKS.csv", "w") as file:
        # Add a header for the CSV
        file.write("Title,Author,ISBN,Year,Price,Quantity\n")
        for book in all_books:
            line = f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            file.write(line)
