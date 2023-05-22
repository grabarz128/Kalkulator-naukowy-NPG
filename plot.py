from sympy import *
from sympy.plotting import plot
x = Symbol('x')


def add_brackets(fun):
    fun_str = '('+str(fun)+')'
    operators = {'+', '-', '*', '/'}
    print(fun_str)

    idx = 0
    idx_frw = 0
    while true:
        idx = fun_str.find('**', idx_frw)
        if idx == -1:
            break
        print(idx)
        idx += 1
        idx_frw = idx + 1
        idx_bck = idx - 2

        while true:
            if fun_str[idx_frw] in operators or fun_str[idx_frw] == '(' or idx_frw == len(fun_str) - 2:
                print(idx_frw)
                break
            idx_frw += 1
        while true:
            if fun_str[idx_bck] in operators or fun_str[idx_bck] == ')' or idx_bck == 0:
                print(idx_bck)
                break
            idx_bck -= 1
        if fun_str[idx_frw] != '(':
            fun_str = fun_str[:idx_frw] + ')' + fun_str[idx_frw:]
        if fun_str[idx_bck] != ')':
            fun_str = fun_str[:idx_bck + 1] + '(' + fun_str[idx_bck + 1:]
        print(fun_str)

    idx = 0
    idx_frw = 0
    while true:
        idx_m = 0
        idx_frw_n = idx_frw
        while fun_str.find('*', idx_frw_n) == fun_str.find('**', idx_frw_n):
            idx_frw_n += 3
            if fun_str.find('*', idx_frw_n) == -1:
                break
        idx_m = fun_str.find('*', idx_frw_n)
        idx_d = fun_str.find('/', idx_frw)
        if idx_d == -1 and idx_m == -1:
            break
        elif idx_m < idx_d and idx_m != -1:
            idx = idx_m
        else:
            idx = idx_d

        #print(idx)
        #print(fun_str[idx])
        idx_frw = idx + 1
        idx_bck = idx - 1
        while true:
            if fun_str[idx_frw] in operators or fun_str[idx_frw] == '(' or idx_frw == len(fun_str) - 1:
                #print(idx_frw)
                #print(fun_str[idx_frw])
                break
            idx_frw += 1
        while true:
            if fun_str[idx_bck] in operators or fun_str[idx_bck] == ')' or idx_bck == 1:
                #print(idx_bck)
                #print(fun_str[idx_bck])
                break
            idx_bck -= 1
        if fun_str[idx_frw] != '(':
            fun_str = fun_str[:idx_frw] + ')' + fun_str[idx_frw:]
        if fun_str[idx_bck] != ')':
            fun_str = fun_str[:idx_bck + 1] + '(' + fun_str[idx_bck+2:]
    #print(fun_str)
    return fun_str


def plt(fun, lim1=-10.0, lim2=10.0, ylim1=-10.0, ylim2=10.0):
    fun_br = add_brackets(fun)
    wykres = plot(fun_br, xlim=[lim1, lim2], ylim=[ylim1, ylim2], line_color='C0', title="", legend=False, xlabel="x", ylabel="y")


plt(log(x)+x**2-3*x+2-10/x)


