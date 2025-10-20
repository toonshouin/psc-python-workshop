def is_number(number = 0):
    if number % 2 == 0:
        if number % 4 !=0 or number % 6 == 0:
            return True
    return False

print(is_number(int(input("Please enter a number: "))))