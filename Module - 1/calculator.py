print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operator = int(input("Select an Operation : "))

num1 = int(input("Input First Number: "))
num2 = int(input("Input Second Number: "))

if operator == 1:
    sum = num1 + num2
    print("Result: " + str(sum))
    
elif operator == 2:
    sub = num1 - num2
    print("Result: " + str(sub))
    
elif operator == 3:
    mul = num1 * num2
    print("Result: " + str(mul))
    
elif operator == 4:
    divi = num1 / num2
    print("Result: " + str(divi))

else:
    print("Invalid Input")
    
    