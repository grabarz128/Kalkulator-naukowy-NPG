# rozwiazywanie wyrazenia z traktowaniem znaku "^" jako potegi
def result(expression):
    n = expression.find("^")
    while n != -1:
        lst = list(expression) + ['']
        lst[n] = lst[n+1] = "*"
        for i in range(n+2, len(lst)):
            lst[i] = expression[i-1]
        expression = ''.join(lst)
        n = expression.find("^")
    print(expression)
    print(eval(expression))


n = str(input())
result(n)