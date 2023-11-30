try:
    number = int(input("Enter an integer:  "))
    print(f"You entered {number}")
except ValueError as ve:
    print("You entered an invalid integer. Please try again.")
    print(f"{ve}")
print("Bye!")

try:
    number = int(input("Enter an integer:  "))
    print(f"You entered {number}")
except:
    print("You entered an invalid integer. Please try again.")
print("Bye!")