
def add (a,b):
    answer = a+b
    print(answer)
def sub (a,b):
    answer = a-b
    print(answer)
def mul (a,b):
    answer = a*b
    print(answer)
def div (a,b):
    answer = a/b
    print(answer)

while True:
    print("Welcome to the basic calculator :)")
    print("Selecct A for Addition")
    print("Selecct S for Subtration")
    print("Selecct M for Multiplication")
    print("Selecct D for Division")
    print("E Exit")

    choice = input("Input your choice: ")

    if choice == "A" or choice == "a":
        a=int(input("input first number: "))
        b=int(input("input second number: "))
        add(a,b)
    elif choice == "S" or choice == "s":
        a=int(input("input first number: "))
        b=int(input("input second number: "))
        sub(a,b)
    elif choice == "M" or choice == "m":
        a=int(input("input first number: "))
        b=int(input("input second number: "))
        mul(a,b)
    elif choice == "D" or choice == "d":
        a=int(input("input first number: "))
        b=int(input("input second number: "))
        div(a,b)
    elif choice == "E" or choice == "e":
        print("cuchau :)")
        quit()