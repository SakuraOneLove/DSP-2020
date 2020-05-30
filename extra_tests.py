"""Тесты для модуля с дополнительными
подпрограммами.
"""
import unittest
import extrafuncs as extras

class TestExtraMethods(unittest.TestCase):
    """Тестирование методов модуля extrafuncs.py
    """
    def test_convert_positiv_decimal_to_bin_without_grid(self):
        self.assertEqual('110', extras.dec2bin(6))
        self.assertEqual('1111', extras.dec2bin(15))

    def test_convert_positiv_decimal_to_bin_with_grid(self):
        self.assertEqual('0111', extras.dec2bin(7, 4))
        self.assertEqual('00101', extras.dec2bin(5, 5))

    def test_convert_negative_decimal_to_bin(self):
        self.assertEqual("1010", extras.dec2bin(-10))

    def test_size_of_bit_grid(self):
        self.assertEqual(4, extras.bit_grid(-8, 7))
        self.assertEqual(5, extras.bit_grid(-14, 9))
        self.assertEqual(8, extras.bit_grid(-70, 120))


if __name__ == "__main__":
    unittest.main()
