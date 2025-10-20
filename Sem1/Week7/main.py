def add(*args) :
    print(args)
    print(args[0])
    print(args[1])

add(1,2,3,4,5)
add(10,20,30)

def add2(*args) :
    result = sum(args)
    return result

group_num1 = add2(10,20,30)
group_input = add2(float(input("Float Number 1 : ")), float(input("Float Number 2 : ")))

print(group_num1)
print(group_input)