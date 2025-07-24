# task1_math_operations.py

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (Cannot divide by zero)"

# Displaying the results
print("\n--- Results ---")
print(f"Addition:= {addition}")
print(f"Subtraction:= {subtraction}")
print(f"Multiplication:{multiplication}")
print(f"Division:= {division}")
