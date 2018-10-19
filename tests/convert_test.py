import unittest

import .currency_convert

class convert_testing():
    convertor = currency_convert.Currency_converter()
    test_dict = {"A": 0, "B": 0.5, "C": 1, "D": 2}
    
    def convert_test_1(self):
        self.assertEqual(convertor.convert(100, ""), 1)
