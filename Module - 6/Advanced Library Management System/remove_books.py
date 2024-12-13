from save_all_books import save_all_books

def remove_books(all_books):
    search_book = input("Enter the title of the book: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books(all_books)
            print(f"{search_book} removed successfully.")
            return all_books
        
    else:
        print(f"{search_book} is not found.")