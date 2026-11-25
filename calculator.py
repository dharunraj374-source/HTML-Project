a=int(input("enter the number: "))
b=int(input("enter the number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        result = "Cannot divide by zero"
    else:
        result = first_number / second_number
else:
    result = "Invalid operator"

print("Result:", result)
