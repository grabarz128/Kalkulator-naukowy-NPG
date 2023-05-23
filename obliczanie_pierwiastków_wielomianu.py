import re

test_input = '3x^3 + 5x^2 + 5x + 15'
test_inpu2 = '-1*x**4 - 3*x**3 + 7*x**2 + 2*x + 15'
# log(x)+x**2-3*x+2-10/x
def return_poly(input):
    potegi_n = re.findall(r"(^[0-9]\*x\**[0-9]|^[+-]*[0-9]\*x\**[0-9] |[+-]\s[0-9]\*x\**[0-9])",input)
    potega1 = re.findall(r"[+-]\s[0-9]\*x\s|[+-]\sx\s",input)
    liczba = re.findall(r"[+-]\s[0-9]{1,5}$",input)
    print(potegi_n)
    print(potega1)
    print(liczba)
    return 0



return_poly(test_inpu2)