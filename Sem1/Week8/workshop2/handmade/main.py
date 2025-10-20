name = input("Please enter your name: ")
score = int(input("Please enter your score: "))

if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"{name}, Your score is {score}, and your grade is {grade}.")