# rozwiazywanie wyrazenia z traktowaniem znaku "^" jako potegi
def result(expression) -> str:
    n = expression.find("^")

    if expression is None:
        return '0'

    while n != -1:
        expression = expression[:n] + "**" + expression[n+1:]
        n = expression.find("^")

    # print(expression)
    solution = eval(expression)
    return solution


if __name__ == '__main__':
    x = str(input())
    print(result(x))