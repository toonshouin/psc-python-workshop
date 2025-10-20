a = float(input("Please enter the first number : "))
b = float(input("Please enter the second number : "))

p = a + b
s = a - b
m = a * b
d = a / b
d_wo_d = a // b
d_d = (a % b) / b
po = a ** b

print(p)
print(s)
print(m)
print(d)
print(d_wo_d)
print(d_d)
print(po)
print(f"The result are Addition is {p}, Subtraction {s}, Multiply {m}, Division {d} are without decimal ({int(d)}) and with decimal ({d_d}) also the exponent is {po}")