a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("hey our programm is not meant to divide numbers by zero")
else:
    print(f"the division a/b is {a/b}")