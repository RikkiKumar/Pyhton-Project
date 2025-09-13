
#Simple calculator
a = int(input("Enter your first number: "))
operator = input("Enter your operator (+,-,*,/): ")
b = int(input("Enter your second number: "))
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed"
else:
    result = "Invalid operator"

print(f"Ther result is {a} {operator} {b} = {result}")





    
