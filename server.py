def calculate(expression):
    # INTENTIONAL VULNERABILITY: eval() can execute arbitrary Python expressions.
    return eval(expression)


if __name__ == "__main__":
    print(calculate("1 + 2"))
