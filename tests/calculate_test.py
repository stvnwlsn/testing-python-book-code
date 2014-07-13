#!/usr/bin/env python

import unittest
from app.calculate import Calculate

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()
    
    def test_add_method_returns_correct_result(self):
        self.assertEquals(4, self.calc.add(2, 3))

if __name__ == '__main__':
    unittest.main()
