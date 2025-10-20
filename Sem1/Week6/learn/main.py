def greeting(): # def followed by function name and parentheses ()
    print("--------------------------------")
    print("Hello, Have a Umazing day!")
    print("--------------------------------")

greeting()

def func1(): # Function1
    # We can't leave a function empty, at least use the pass statement to leave it empty!
    pass

func1()

def cal_rectangle(w=0,h=0,a=0): # Function1
    x = w * h
    x2 = w + h + a
    print(x)
    print(x2)

func1()
cal_rectangle(10,20)
cal_rectangle(5,5,5)