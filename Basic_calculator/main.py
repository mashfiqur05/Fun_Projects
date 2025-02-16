def add(*args):
    result = sum(args)
    print(f"{' + '.join(map(str, args))} = {result}\n")

def sub(*args):
    result = args[0] - sum(args[1:])
    print(f"{' - '.join(map(str, args))} = {result}\n")

def multi(*args):
    result = 1
    for num in args:
        result *= num
    print(f"{' * '.join(map(str, args))} = {result}\n")

def div(*args):
    try:
        result = args[0]
        for num in args[1:]:
            result /= num
        print(f"{' / '.join(map(str, args))} = {result}\n")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Input your choice: ")

    if choice.lower() in ['a', 'b', 'c', 'd']:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if not numbers:
            print("Please enter valid numbers.\n")
            continue
        
        if choice.lower() == 'a':
            add(*numbers)
        elif choice.lower() == 'b':
            sub(*numbers)
        elif choice.lower() == 'c':
            multi(*numbers)
        elif choice.lower() == 'd':
            div(*numbers)
    elif choice.lower() == 'e':
        print("Program is closing...")
        break
    else:
        print("Input a valid choice.\n")
