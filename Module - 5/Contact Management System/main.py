from add_contract import add_contract
from view_contract import view_contract
from remove_contract import remove_contract
from search_contract import search_contract

def main():
    while True:
        print("\nWelcome to Contact Book Management System\n")

        print("1. Add Contract")
        print("2. View all Contracts")
        print("3. Remove Contract")
        print("4. Search Contract")
        print("0. Exit")
        
        choice = input("Enter an operation: ")
        
        if choice == "1":
            try:
                name = input("Enter name: ")
                if not name.isalpha():
                    raise ValueError("Name must only contain alphabetic characters.")
                
                email = input("Enter email: ")
                if "@" not in email or "." not in email:
                    raise ValueError("Please provide a valid email address.")
                
                phone_num = input("Enter phone number: ")
                if not phone_num.isdigit():
                    raise ValueError("Phone number must contain only digits.")
                
                address = input("Enter address: ")
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                nationality = input("Enter nationality: ")
                
                # Add contact
                add_contract(name, email, phone_num, address, date_of_birth, nationality)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == "2":
            view_contract()
            
        elif choice == "3":
            try:
                index = int(input("Enter the index number of the contact you want to remove: "))
                remove_contract(index)
            except ValueError:
                print("Please enter a valid integer index.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            
        elif choice == "4":
            query = input("Enter the keyword you want to search: ").lower()
            search_contract(query)
            
        elif choice == "0":
            print("Thank you for using this app.")
            break
        
        else:
            print("Invalid option. Please choose a valid operation.")


if __name__ == "__main__":
    main()