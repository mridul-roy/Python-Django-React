import add_books
import save_all_books
import view_all_books

all_books = []

while True:
    print("\nWelcome to Library Management System!!!")
    print("1. Add Books")
    print("2. View all Books")
    print("0. Exit")
    
    option = input("Enter an Option: ")
    
    if option == "0":
        print("Thank you.")
        break
    elif option == "1":
        all_books = add_books.add_books(all_books)
    elif option == "2":
        view_all_books.view_all_books(all_books)
    else:
        print("Invalid choice!")
