import json

def save_all_books(all_books):
    with open ("all_books.json", "w") as file:
        json.dump(all_books,file, indent=4)
        

def save_lend_books(lend_books):
    with open ("lend_books.json","w") as file:
        json.dump(lend_books,file, indent=4)