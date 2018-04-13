#Zhukov V.N.
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


if __name__ == "__main__":
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
        except:
            print("That is not a number!")
            continue

        operator = input("Enter an operator (valid operators are +, -, *, / and pow): ")

        if operator == "+":
            func = add
        elif operator == "-":
            func = sub
        elif operator == "*":
            func = mul
        elif operator == "/":
            func = div
        else:
            print("Invalid operator!")
            continue

        print(func(number1, number2))
