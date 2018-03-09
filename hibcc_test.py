# -*- coding: utf-8 -*-
"""
This module tests for HIBCC barcode module.
"""
import sys
import hibcc
import unittest


class testFunctions(unittest.TestCase):
    def setUp(self):
        self.code = "+E1782617400501B"
        self.wrong_code = "+E1782617400502B"
        self.wrong_code2 = "+E17"
        self.lot = "+$2034000BE"
        self.wrong_lot = "+2034000BE"
        self.lic = "E178"
        self.catalog_number = "261740050"
        self.unit_of_measure = "1"

    def test_get_lic(self):
        self.assertEqual(hibcc.get_lic(self.code), "E178")

    def test_check_lic_length(self):
        self.assertEqual(hibcc.check_lic_length(self.code), True)
        self.assertEqual(hibcc.check_lic_length(self.wrong_code2), False)

    def test_calculate_checkdigit(self):
        self.assertEqual(hibcc.calculate_checkdigit(self.code), 'B')

    def test_get_checkdigit(self):
        self.assertEqual(hibcc.get_checkdigit(self.code), 'B')

    def test_create_catalog_code(self):
        self.assertEqual(hibcc.create_catalog_code(
            self.lic, self.catalog_number, self.unit_of_measure), self.code)

    def test_check_lot_code_start(self):
        self.assertEqual(hibcc.check_lot_code_start(self.lot), True)
        self.assertEqual(hibcc.check_lot_code_start(self.wrong_lot), False)

    def test_get_lot_number(self):
        self.assertEqual(hibcc.get_lot_number(self.lot), "2034000")
        self.assertEqual(hibcc.get_lot_number(self.lot, True), "2034")

    def test_get_link_char_from_catalog_code(self):
        self.assertEqual(hibcc.get_link_char_from_catalog_code(self.code), 'B')

    def test_get_link_char(self):
        self.assertEqual(hibcc.get_link_char(self.lot), 'B')


if __name__ == '__main__':
    unittest.main()
