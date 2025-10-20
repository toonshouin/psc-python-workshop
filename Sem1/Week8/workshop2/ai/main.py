name = input("Please enter your name: ")
score = int(input("Please enter your score: "))

# กำหนดเกรดแบบสั้นโดยใช้ list comprehension และ next()
grade = next((g for s, g in [(80, 'A'), (70, 'B'), (60, 'C'), (50, 'D')] if score >= s), 'F')

print(f"{name}, Your score is {score}, and your grade is {grade}.")
