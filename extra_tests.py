"""Тесты для модуля с дополнительными
подпрограммами.
"""
import unittest
import extrafuncs as extras

class TestExtraMethods(unittest.TestCase):
    """Тестирование методов модуля extrafuncs.py
    """
    def setUp(self):
        """Установка начальных параметров для тестирования.
        """
        self.decimal_arr = [-8, -7, 1, 2]
        self.compl_arr = ["1000 (-8)", "1001 (-7)", "0001 (1)", "0010 (2)"]

    def test_convert_positiv_decimal_to_bin_without_grid(self):
        """Проверка перевода положительных и отрицательных чисел из
        десятичной СС в двоичную.
        """
        self.assertEqual('110', extras.dec2bin(6))
        self.assertEqual('1111', extras.dec2bin(15))

    def test_convert_positiv_decimal_to_bin_with_grid(self):
        """Проверка перевода положительных и отрицательных чисел из
        десятичной СС в двоичную.
        """
        self.assertEqual('0111', extras.dec2bin(7, 4))
        self.assertEqual('00101', extras.dec2bin(5, 5))

    def test_convert_negative_decimal_to_bin(self):
        """Проверка перевода положительных и отрицательных чисел из
        десятичной СС в двоичную.
        """
        self.assertEqual("1010", extras.dec2bin(-10))

    def test_size_of_bit_grid(self):
        """Проверка определения размера разрядной сетки
        для чисел, переводимых в дополнительный код.
        """
        self.assertEqual(4, extras.bit_grid(-8, 7))
        self.assertEqual(5, extras.bit_grid(-14, 9))
        self.assertEqual(8, extras.bit_grid(-70, 120))

    def test_convert_decimal_arr_to_first_complement_arr(self):
        """Проверка правильности трансляции десятичного массива
        в массив дополнительных чисел.
        """
        self.assertEqual(self.compl_arr,\
            extras.dec2compl(self.decimal_arr))

if __name__ == "__main__":
    unittest.main()
