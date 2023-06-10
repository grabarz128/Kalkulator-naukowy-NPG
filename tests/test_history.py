#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from kalkulator import *

class HistoryTest(unittest.TestCase):
    def setUp(self):
        self.window = calculator()
        self.cell = calc_cell(self.window)
        self.buttons = calc_buttons(self.window, self.cell)
    def test_history(self):
        for x in range(10):
            self.buttons[12].invoke()
            self.buttons[-1].invoke()
            self.buttons[5].invoke()
        self.buttons[13].invoke()
        self.buttons[-1].invoke()
        self.assertEqual(wpisy, ['2 = 2', '1 = 1', '1 = 1', '1 = 1', '1 = 1', '1 = 1', '1 = 1', '1 = 1', '1 = 1', '1 = 1'])

