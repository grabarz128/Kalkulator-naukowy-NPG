# rozwiazywanie wyrazenia z traktowaniem znaku "^" jako potegi
def result(expression):
    n = expression.find("^")

    while n != -1:
        expression = expression[:n] + "**" + expression[n+1:]
        n = expression.find("^")
    print(expression)
    print(eval(expression))


n = str(input())
result(n)