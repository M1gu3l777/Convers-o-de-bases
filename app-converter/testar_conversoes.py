
import unittest
from conversoes import converter


class TestConversoes(unittest.TestCase):

    def test_decimal_para_binario(self):
        self.assertEqual(converter("13", 10, 2), "1101")

    def test_decimal_para_hexadecimal(self):
        self.assertEqual(converter("255", 10, 16), "FF")

    def test_binario_para_decimal(self):
        self.assertEqual(converter("1101", 2, 10), "13")

    def test_binario_para_hexadecimal(self):
        self.assertEqual(converter("11111111", 2, 16), "FF")

    def test_hexadecimal_para_binario(self):
        self.assertEqual(converter("FF", 16, 2), "11111111")

    def test_hexadecimal_para_decimal(self):
        self.assertEqual(converter("FF", 16, 10), "255")

    def test_octal_para_binario(self):
        self.assertEqual(converter("17", 8, 2), "1111")

    def test_octal_para_decimal(self):
        self.assertEqual(converter("17", 8, 10), "15")

    def test_octal_para_hexadecimal(self):
        self.assertEqual(converter("17", 8, 16), "F")

    def test_numero_binario_invalido(self):
        with self.assertRaises(ValueError):
            converter("102", 2, 10)


if __name__ == "__main__":
    unittest.main()
