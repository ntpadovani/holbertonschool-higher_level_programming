#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for Test Max Integer"""


    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-5, -9, 0, -4]), 0)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)

    def test_max_boolean(self):
        self.assertTrue(max_integer([True, False]), True)

    def test_max_string(self):
        self.assertEqual(max_integer(["hola"]), "hola")