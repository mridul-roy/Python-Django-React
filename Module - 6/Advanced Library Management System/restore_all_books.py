import json

def restore_all_books(all_books):
    with open("all_books.json","r") as file:
        all_books = json.load(file)
    return all_books