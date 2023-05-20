from sympy import *
from sympy.plotting import plot
x = Symbol('x')


def plt(fun, lim1=-10, lim2=10):
    wykres = plot(fun, (x, lim1, lim2))
    print("jestem")
    wykres.show()


plt(x**2)
