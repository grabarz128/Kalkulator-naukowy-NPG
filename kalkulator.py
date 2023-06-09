#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk

from sympy import *
from sympy.plotting import plot
x = Symbol('x')

import matplotlib
matplotlib.use("TkAgg")

from plot import *
from liczenie import *
from remember import *
from math import *



def calculator(): #tworzy okno kalkulatora
    window = tk.Tk()
    window.geometry('400x500')
    window.title('KALKULATOR PROSTY')
    window.configure(bg='LightSkyBlue1')
    return window

window = calculator()

def calc_cell(window): #komórka do wpisywania obliczeń
    cell = tk.Entry(window, borderwidth = 3, highlightcolor = 'white', justify = 'center')
    cell.grid(row = 1, columnspan = 6, ipadx = 50, ipady = 10)
    window.grid_columnconfigure(0, weight=1)
    cell.configure(font=("Calibri", 14))

    return cell

def calculate(cell):    #funkcja obliczająca wyrażenie
    expression = cell.get()
    res = str(expression) + ' = ' + str(result(expression))
    remember(wpisy, res)
    cell.delete(0, tk.END)
    cell.insert(tk.END, str(res))

def calc_buttons(window, cell): #ustawia ustawia cyfry i operatory działań
    buttons = []

    button_7 = tk.Button(window, text='7', bg='white', borderwidth=0, command=lambda: put_button('7'))
    button_7.grid(row=3, column=0, ipadx=10, ipady=5)
    button_7.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_7)

    button_8 = tk.Button(window, text='8', bg='white', borderwidth=0, command=lambda: put_button('8'))
    button_8.grid(row=3, column=1, ipadx=10, ipady=5)
    button_8.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_8)

    button_9 = tk.Button(window, text='9', bg='white', borderwidth=0, command=lambda: put_button('9'))
    button_9.grid(row=3, column=2, ipadx=10, ipady=5)
    button_9.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_9)

    button_divide = tk.Button(window, text='/', bg='white', borderwidth=0, command=lambda: put_button(' / '))
    button_divide.grid(row=3, column=3, ipadx=10, ipady=5)
    button_divide.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_divide)

    button_back = tk.Button(window, text='\u21BA', bg='white', borderwidth=0, command=lambda: last())
    button_back.grid(row=3, column=4, ipadx=10, ipady=5)
    button_back.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_back)

    button_clr = tk.Button(window, text='C', bg='white', borderwidth=0, command=lambda: clear())
    button_clr.grid(row=3, column=5, ipadx=10, ipady=5)
    button_clr.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_clr)

    button_4 = tk.Button(window, text='4', bg='white', borderwidth=0, command=lambda: put_button('4'))
    button_4.grid(row=4, column=0, ipadx=10, ipady=5)
    button_4.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_4)

    button_5 = tk.Button(window, text='5', bg='white', borderwidth=0, command=lambda: put_button('5'))
    button_5.grid(row=4, column=1, ipadx=10, ipady=5)
    button_5.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_5)

    button_6 = tk.Button(window, text='6', bg='white', borderwidth=0, command=lambda: put_button('6'))
    button_6.grid(row=4, column=2, ipadx=10, ipady=5)
    button_6.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_6)

    button_multiply = tk.Button(window, text='*', bg='white', borderwidth=0, command=lambda: put_button('*'))
    button_multiply.grid(row=4, column=3, ipadx=10, ipady=5)
    button_multiply.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_multiply)

    button_leftbracket = tk.Button(window, text='(', bg='white', borderwidth=0, command=lambda: put_button('('))
    button_leftbracket.grid(row=4, column=4, ipadx=10, ipady=5)
    button_leftbracket.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_leftbracket)

    button_rightbracket = tk.Button(window, text=')', bg='white', borderwidth=0,command=lambda: put_button(')'))
    button_rightbracket.grid(row=4, column=5, ipadx=10, ipady=5)
    button_rightbracket.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_rightbracket)

    button_1 = tk.Button(window, text='1', bg='white', borderwidth=0, command=lambda: put_button('1'))
    button_1.grid(row=5, column=0, ipadx=10, ipady=5)
    button_1.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_1)

    button_2 = tk.Button(window, text='2', bg='white', borderwidth=0, command=lambda: put_button('2'))
    button_2.grid(row=5, column=1, ipadx=10, ipady=5)
    button_2.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_2)

    button_3 = tk.Button(window, text='3', bg='white', borderwidth=0, command=lambda: put_button('3'))
    button_3.grid(row=5, column=2, ipadx=10, ipady=5)
    button_3.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_3)

    button_minus = tk.Button(window, text='-', bg='white', borderwidth=0, command=lambda: put_button('-'))
    button_minus.grid(row=5, column=3, ipadx=10, ipady=5)
    button_minus.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_minus)

    button_pow = tk.Button(window, text='x^2', bg='white', borderwidth=0,command=lambda: put_button('^2 '))
    button_pow.grid(row=5, column=4, ipadx=10, ipady=5)
    button_pow.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_pow)

    button_sqrt = tk.Button(window, text='\u221Ax', bg='white', borderwidth=0, command=lambda: put_button('**(0.5)'))
    button_sqrt.grid(row=5, column=5, ipadx=10, ipady=5)
    button_sqrt.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_sqrt)

    button_0 = tk.Button(window, text='0', bg='white', borderwidth=0, command=lambda: put_button('0'))
    button_0.grid(row=6, column=0, ipadx=10, ipady=5)
    button_0.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_0)

    button_comma = tk.Button(window, text=',', bg='white', borderwidth=0, command=lambda: put_button(','))
    button_comma.grid(row=6, column=1, ipadx=10, ipady=5)
    button_comma.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_comma)

    button_percent = tk.Button(window, text='%', bg='white', borderwidth = 0, command=lambda: put_button('%'))
    button_percent.grid(row=6, column=2, ipadx=10, ipady=5)
    button_percent.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_percent)

    button_plus = tk.Button(window, text='+', bg='white', borderwidth=0,command=lambda: put_button(' + '))
    button_plus.grid(row=6, column=3, ipadx=10, ipady=5)
    button_plus.configure(width=5, height=2, font=("Calibri", 13))
    buttons.append(button_plus)

    equal_sign = tk.Button(window, text='=', bg='white', borderwidth=0, command=lambda: calculate(cell))
    equal_sign.grid(row=6, column=4, columnspan=2, ipadx=64, ipady=21)

    buttons.append(equal_sign)

    return buttons
'''
    j = 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1
        margin = 0 if len(symbols[i]) == 1 else 10
        buttons[i].grid(row=j, column=i % 6,  ipady=5)
'''

def put_button(sign):    #funkcja dodająca wcisniete przyciski
    expression = cell.get()
    res = str(expression) + sign
    cell.delete(0, tk.END)
    cell.insert(tk.END, str(res))

def clear():  #funkcja czyszczaca pole do wpisywania
    cell.delete(0, tk.END)

def last(): #funkcja zwracająca ostatnie równanie
    cell.delete(0, tk.END)
    cell.insert(tk.END, wpisy[0])
    
    
def history_btn(window): #button przejścia do historii
    def open_history_window(): #okno z histrią
        history= tk.Toplevel()
        history.geometry('398x650')
        history.title('HISTORIA')
        history.configure(bg='LightSkyBlue1')
        history_windows = []
        for i in range(10):
            history_window = tk.Text(history, height=3, width=48, borderwidth=1, relief='raised')
            history_window.grid(row = i, column = 0, padx=5, pady=2, sticky = 'w' )
            history_windows.append(history_window)
            history_window.configure(font=("Calibri", 12))
            history_window.insert(tk.END, '\n' + wpisy[i])
            history_window.tag_configure( "center", justify='center')
            history_window.tag_add("center", "1.0", "end")
        return history_windows
        def get_history(history_windows):
            for i in range(10):
                if i < len(wpisy):
                    history_windows[i].delete('1.0', tk.END)
                    history_windows[i].insert(tk.END,'\n' + wpisy[i], justify='center')
                    history_windows[i].tag_add("center", "1.0", "end")

        get_history(history_windows)

    history_button = tk.Button(window, text='HISTORIA', bg='LightSkyBlue1', borderwidth=1, command=open_history_window)
    history_button.grid(row=10, column=0, columnspan=6, ipadx=20, ipady=20, pady=10)
    window.grid_columnconfigure(2, weight=1)

    return history_button


def open_graph_window():
    graph_window = tk.Toplevel()
    graph_window.geometry('400x100')
    graph_window.title('KALKULATOR GRAFICZNY')
    graph_window.configure(bg='LightSkyBlue1')
    return graph_window

g_cell_value = tk.StringVar(window)
def calc_graph_cell(graph_window):
    g_cell = tk.Entry(graph_window, borderwidth=3, highlightcolor='white', justify='center', textvariable=g_cell_value)
    g_cell.grid(row=1, columnspan=6, ipadx=50, ipady=10)
    graph_window.grid_columnconfigure(0, weight=1)
    g_cell.configure(font=("Calibri", 14))
    #g_cell_value = g_cell.get()
    return g_cell #, g_cell_value

def graph_this_btn(graph_window):
    button = tk.Button(graph_window, text='Pokaż wykres', command=plot_this)
    button.grid(row=6, column=0, ipadx=10, ipady=5)
    return button


def graph_btn(window): #button przejścia do graficznego
        def open_graph_window2():
        graph_window = open_graph_window()
        graph_this_button = graph_this_btn(graph_window)
        graph_cell = calc_graph_cell(graph_window)

    graph_button = tk.Button(window, text='KALKULATOR GRAFICZNY', bg='LightSkyBlue1', borderwidth=1, command=open_graph_window2)
    graph_button.grid(row=40, column=0, columnspan=6, ipadx=20, ipady=20, pady=10)
    window.grid_columnconfigure(2, weight=1)

    return graph_button


def plot_this():
    plt(g_cell_value.get())
    print(g_cell_value.get())


if __name__ == '__main__':
    cell = calc_cell(window)
    buttons = calc_buttons(window, cell)
    graph_button = graph_btn(window)
    history_button = history_btn(window)


    window.mainloop()
