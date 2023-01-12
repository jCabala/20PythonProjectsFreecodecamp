def add(a, b):
    print(f"{a} + {b} = {a+b}")

def sub(a, b):
    print(f"{a} - {b} = {a-b}")

def mult(a, b):
    print(f"{a} * {b} = {a*b}")

def div(a, b):
    if b == 0:
        print("Do not divide by zero!")
    else:
        print(f"{a} / {b} = {a/b}")

while(True):
    a = input("Input a\n")
    b = input("Input b\n")
    op = input("Input add, sub, mult or div\n")
    ops = {"add": add, "sub": sub, "mult": mult, "div": div}
    if op in ops.keys():
        ops[op](float(a),float(b))
    else:
        print("Wrong operation! Operation not supported!")

    runAgain = input("Run again? [y/n]")
    if runAgain != "y":
        quit()
