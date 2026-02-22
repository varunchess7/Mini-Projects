import math

while True:
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    choice = int(input("Enter your choice: "))

    def addition():
        num1 = int(input("Enter Num1: "))
        num2 = int(input("Enter Num2: "))
        sum = num1 + num2
        print(sum)

    def subtraction():
        num1 = int(input("Enter Num1: "))
        num2 = int(input("Enter Num2: "))
        diff = num1 - num2
        print(diff)

    def multiplication():
        num1 = int(input("Enter Num1: "))
        num2 = int(input("Enter Num2: "))
        mult = num1 * num2
        print(mult)

    def division():
        num1 = int(input("Enter Num1: "))
        num2 = int(input("Enter Num2: "))
        div = num1 / num2
        print(div)

    def root():
        num1 = int(input("Enter Num1: "))
        root = math.sqrt(num1)
        print(root)

    def exponent():
        num1 = int(input("Enter Num1: "))
        power = int(input("Enter Power: "))
        powerc = num1**power
        print(powerc)


    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        exponent()
    elif choice == 6:
        root()