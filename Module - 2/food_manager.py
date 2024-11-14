print("Welcome to Favourite Food Manager!!!")

favorite_foods = [] # hold data if user add any items

while True:
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View all Foods")
    print("0. Exit\n")
    
    choice = input("Enter an Operation: ") # Take user input for an operation
    
    if choice == "0":
        print("Thank You for Using Favourite Foods App.")
        break
    
    elif choice == "1":
        food = input("Enter the name of Food: ").lower()
        favorite_foods.append(food)
        print(f"{food}, Successfully Added.")
        
    elif choice == "2":
        food = input("Enter the Name of the Food which want to remove: ").lower()
        if food in favorite_foods:
            favorite_foods.remove(food)
            print(f"{food}, removed Successfully.")
        else:
            print(f"{food} is not exist in list.")
        
    elif choice == "3":
        if len(favorite_foods) != 0:
            for index in enumerate(favorite_foods, start=1):
                print(f"{index}")
        else:
            print("List is empty.")
        
    else:
        print("Invalide Choise")
        
        