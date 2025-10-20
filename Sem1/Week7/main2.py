def add(**kwargs):
    print(kwargs)

add(a=1, b=2, c=3)
add(x = 100, y = 200)

def add2(*args) :
    print(args)

add(1,2,3)