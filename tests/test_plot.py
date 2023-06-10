#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from kalkulator import *

class OperatorsTest(unittest.TestCase):
    def setUp(self):
        self.window = calculator()
        self.cell = calc_cell(self.window)
        self.buttons = calc_buttons(self.window, self.cell)

    def test_power(self):
        self.assertEqual(power('x^2'), 'x**2')

    def test_add_brackets(self):
        self.assertEqual(add_brackets('x+1/x+2*x+x**2'), '(x+(1/x)+(2*x)+(x**2))')