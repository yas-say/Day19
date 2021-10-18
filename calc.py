def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


a = int(input("1st Number: "))
operation = input("What operation(add/sub/mul/div): ")
b = int(input("2nd Number: "))

print(calculator(a, b, add))
