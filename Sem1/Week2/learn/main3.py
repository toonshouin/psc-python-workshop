# first_name = "Kritthapath"

firstname_input = input("What's your first name? : ")
age = 18

result1 = firstname_input + str(age) # Concatenating string and integer using str()
result2 = f"{firstname_input} + {age}" # Using f-string for formatting and concatenation

print(result1)
print(result2)