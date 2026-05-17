# So hey welcome again to a better calculatorusing elif.

print("Hi welcome to Python Calculator-2 \n Made buy :- Vansh Kulshreshtha")

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

x = input("Enter the operation you want to perform ( +, -, *, /, ^, mod, //(for floor division)): ")

if (x == "+"):
    print("The sum of", a, "and", b, "is", a + b)
elif (x == "-"):
    print("The difference of", a, "and", b, "is", a - b)
elif (x=="*"):
        print("The product of", a, "and", b, "is", a * b)
elif (x== "/"):
    print("The value of", a, "divided by", b, "is", a / b)
elif (x == "^"):
    print("The value of", a, "raised to the power", b, "is", a ** b)
elif (x == "mod"):
    print("The remainder when", a, "is divided by", b, "is", a % b)
elif (x == "//"):
    print("The floor division of", a, "and", b, "is", a // b)
else:
    print("The operation is not valid. Please enter a valid operation.")


# In the above code, we take two numbers as input and then ask the user to enter the operation they want to perform.
# We use an if-elif-else statement to check which operation the user has chosen and perform the corresponding calculation.
# If the user enters an invalid operation, we print a message indicating that the operation is not valid. 



