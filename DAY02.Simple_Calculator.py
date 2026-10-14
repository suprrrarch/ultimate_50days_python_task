
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operator:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operator = input("Enter operator: ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid operator!")
