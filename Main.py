try:
    age = int(input("Enter your age: "))
    print(f"Your age is:{age}")
except ValueError as ex:
    print(f"Error:please enter a number not a letter")