def addition(a,b):
    try:
        return a+b
    except TypeError as e:
        print(f"Exception:{e}")
    return
def subtraction(a,b):
    try:
        return a-b
    except TypeError as e:
        print(f"Exception:{e}")
    return
def multiplication(a,b):
    try:
        return a*b
    except TypeError as e:
        print(f"Exception:{e}")
    return
def division(a,b):
    try:
        if b==0:
            raise ZeroDivisionError("Divisible by '0' is infinite." )
        return a/b
    except (TypeError,ZeroDivisionError) as e:
        print(f"Exception:{e}")
    return

while True:
    def get_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    a = get_input("\nEnter the first number: ")
    b = get_input("Enter the second number: ")
    op = input("Choose the Operator (+, -, *, /): ")
    print()
    if(op == '+'):
        print(f'The addition of {a} and {b} is {addition(a,b)}')
    elif(op == '-'):
        print(f'The subtraction of {a} and {b} is {subtraction(a,b)}')
    elif(op == '*'):
        print(f'The multiplication of {a} and {b} is {multiplication(a,b)}')
    elif(op == '/'):
        print(f'The division of {a} and {b} is {division(a,b)}')
    else:
        print("Invalid operator. Please enter valid operator.")
    print('\nDo you want to calculate again?')
    next_op=int(input("select '1' or '0' (1.yes/0.no): "))
    try:
        if next_op==0 or next_op!=1:
            break
    except ValueError:
        print('Invalid option.Enter 1 or 0.')
        

print()