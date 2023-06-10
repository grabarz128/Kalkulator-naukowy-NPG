#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from kalkulator import *

class PlotTest(unittest.TestCase):
    def setUp(self):
        self.window = calculator()
        self.cell = calc_cell(self.window)
        self.buttons = calc_buttons(self.window, self.cell)

    def test_power(self):
        self.assertEqual(power('x^2'), 'x**2')

    def test_add_brackets(self):
        self.assertEqual(add_brackets('log(x)+x**2-3*x+2-10/x'), '(log(x)+(x**2)-(3*x)+2-(10/x))')
