#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from kalkulator import *

class OperatorsTest(unittest.TestCase):
    def setUp(self):
        self.window = calculator()
        self.cell = calc_cell(self.window)
        self.buttons = calc_buttons(self.window, self.cell)

    def test_clear(self):
        self.buttons[12].invoke()
        self.buttons[-1].invoke()
        self.buttons[5].invoke()
        self.assertEqual(self.cell.get(), '')

    def test_last(self):
        self.buttons[12].invoke()
        self.buttons[-1].invoke()
        self.buttons[5].invoke()
        self.buttons[4].invoke()
        self.assertEqual(self.cell.get(), '1 = 1')
    def test_addition(self):
        self.buttons[13].invoke()
        self.buttons[21].invoke()
        self.buttons[12].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '2+1 = 3')

    def test_subraction(self):
        self.buttons[13].invoke()
        self.buttons[15].invoke()
        self.buttons[12].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '2-1 = 1')

    def test_multiplication(self):
        self.buttons[13].invoke()
        self.buttons[9].invoke()
        self.buttons[13].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '2*2 = 4')

    def test_division(self):
        self.buttons[6].invoke()
        self.buttons[3].invoke()
        self.buttons[13].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '4/2 = 2.0')

    def test_square(self):
        self.buttons[13].invoke()
        self.buttons[16].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '2^2 = 4')

    def test_sqrt(self):
        self.buttons[6].invoke()
        self.buttons[17].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '4**(0.5) = 2.0')

    def test_mod2(self):
        self.buttons[14].invoke()
        self.buttons[20].invoke()
        self.buttons[13].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '3%2 = 1')

    def test_brackets(self):
        self.buttons[13].invoke()
        self.buttons[9].invoke()
        self.buttons[10].invoke()
        self.buttons[12].invoke()
        self.buttons[21].invoke()
        self.buttons[13].invoke()
        self.buttons[11].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '2*(1+2) = 6')

    def test_comma(self):
        self.buttons[18].invoke()
        self.buttons[19].invoke()
        self.buttons[13].invoke()
        self.buttons[9].invoke()
        self.buttons[7].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(self.cell.get(), '0.2*5 = 1.0')
