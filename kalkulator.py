#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk

from sympy import *
from sympy.plotting import plot
x = Symbol('x')

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from plot import *

def calculator(): #tworzy okno kalkulatora
    window = tk.Tk()

    window.geometry('420x800')
    window.title('Kalkulator prosty')
    window.configure(bg='LightSkyBlue1')

    return window


def calc_cell(window): #komórka do wpisywania obliczeń
    cell = tk.Entry(window, borderwidth = 3, highlightcolor = 'white', justify = 'center')
    cell.grid(row = 1, columnspan = 6, ipadx = 50, ipady = 10)
    window.grid_columnconfigure(0, weight=1)
    cell.configure(font=("Calibri", 14))

    return cell



def calc_buttons(window, cell): #ustawia ustawia cyfry i operatory działań
    symbols = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221Ax',
               '0', ',', '%', '+']

    buttons = [tk.Button(window, text = icon, bg = 'white', borderwidth = 0) for icon in symbols]

    j = 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1

        margin = 10 if len(symbols[i]) == 1 else 10
        buttons[i].grid(row = j, column = i % 6, ipadx = margin, ipady = 5)
        buttons[i].configure(width=5, height=2, font=("Calibri", 13))

    equal_sign = tk.Button(window, text = '=', bg = 'white', borderwidth = 0)
    equal_sign.grid(row = 6, column = 4, columnspan = 2, ipadx = 64, ipady = 21)


    return buttons


def calc_history(window): #10 ostatnich obliczeń
    history_text = tk.Label(window, bg='LightGrey', text='Historia:')
    history_text.grid(row = 7, column = 1)
    history_text.configure(font=("Calibri", 12)) #sam napis "Historia"

    history_windows = []
    for i in range(10):
        history_window = tk.Text(window, height=3, width=20, borderwidth=1, relief='raised')
        history_window.grid(row=8 + (i // 2) * 6, column=(i % 2) * 3 + 1, columnspan=2, padx=5, pady=5, sticky='w')
        history_windows.append(history_window)
        history_window.configure(font=("Calibri", 12))


    return history_text, history_windows

def graph_btn(window): #button przejścia do graficznego
    def open_graph_window():
        graph_window = tk.Toplevel()
        graph_window.geometry('500x600')
        graph_window.title('Kalkulator graficzny')
        graph_window.configure(bg='LightSkyBlue1')
        return graph_window

    graph_window = open_graph_window()

    graph_button = tk.Button(window, text='Kalkulator graficzny', bg='LightSkyBlue1', borderwidth=1, command=open_graph_window)
    graph_button.grid(row=40, column=1, columnspan=6, ipadx=20, ipady=20, pady=10)
    window.grid_columnconfigure(2, weight=1)

    def calc_cell(graph_window):
        g_cell = tk.Entry(graph_window, borderwidth=3, highlightcolor='white', justify='center')
        g_cell.grid(row=1, columnspan=6, ipadx=50, ipady=10)
        graph_window.grid_columnconfigure(0, weight=1)
        g_cell.configure(font=("Calibri", 14))
        return g_cell

    return graph_button, graph_window

def plot_this():
    fun = calc_cell(graph_btn(window)[1])
    wykres = plt(fun)
    wykres.show()


#button_plt = tk.Button(graph_window, text='Pokaż wykres', command=plot_this())
#button_plt.grid(row=6, column=4, columnspan=2, ipadx=64, ipady=21)

if __name__ == '__main__':
    window = calculator()
    cell = calc_cell(window)
    buttons = calc_buttons(window, cell)
    history_text = calc_history(window)
    graph_button, graph_window = graph_btn(window)

    g_cell = calc_cell(graph_window)

    window.mainloop()