def add(n1, n2):
    return n1 + n2


def substruct(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substruct,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
    operation_symbol = input("pick an operation")
    calculate = operations[operation_symbol]
    answer = calculate(num1, num2)

    print(f"the asnwer is {answer}")

calculator()