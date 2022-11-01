#!/usr/bin/python3
"""Unittest cases por square.py"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
from contextlib import redirect_stdout as out
import io
import os


class TestSquare(unittest.TestCase):
    """
    Args:
        unittest
    """
    pass

    def setUp(self):
        """ print('setUp') """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_sqr_id(self):
        """OK"""
        sq = Square(5)
        self.assertEqual(sq.id, 1)
        sq = Square(2, 1)
        self.assertEqual(sq.id, 2)
        sq = Square(10, 0, 0, 55)
        self.assertEqual(sq.id, 55)

    def test_subcls(self):
        """sub class"""
        sq = Square(10, 2)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_width(self):
        """sq width"""
        sq = Square(5)
        self.assertEqual(sq.width, 5)

    def test_size(self):
        """sq size"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)

    def test_err_size(self):
        """size 0"""
        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_x(self):
        """x"""
        sq = Square(10, 2)
        self.assertEqual(sq.x, 2)
        sq = Square(10, 3, 2, 5)
        self.assertEqual(sq.x, 3)
        sq = Square(3, 1, 0)
        self.assertEqual(sq.x, 1)

    def test_x_neg(self):
        """negative x"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1)

    def test_x_str(self):
        """str as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, '')

    def test_x_dict(self):
        """dict as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, {})

    def test_x_tup(self):
        """tuple as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, ())

    def test_x_list(self):
        """list as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, [])

    def test_x_float(self):
        """float as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3.14159)

    def test_x_none(self):
        """none as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, None)

    def test_x_set(self):
        """set as x"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, {1})

    def test_w_neg(self):
        """negative width"""
        with self.assertRaises(ValueError):
            r = Square(-2)

    def test_w_str(self):
        """str as width"""
        with self.assertRaises(TypeError):
            r = Square('')

    def test_w_dict(self):
        """dict as width"""
        with self.assertRaises(TypeError):
            r = Square({})

    def test_w_tup(self):
        """tuple as width"""
        with self.assertRaises(TypeError):
            r = Square(())

    def test_w_list(self):
        """list as width"""
        with self.assertRaises(TypeError):
            r = Square([])

    def test_w_float(self):
        """float as width"""
        with self.assertRaises(TypeError):
            r = Rectangle(3.14159)

    def test_w_none(self):
        """none as width"""
        with self.assertRaises(TypeError):
            r = Rectangle(None)

    def test_w_set(self):
        """set as width"""
        with self.assertRaises(TypeError):
            r = Rectangle({1})

    def test_y_neg(self):
        """negative y"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 1, -1)

    def test_y_str(self):
        """str as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 1, '')

    def test_y_dict(self):
        """dict as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {})

    def test_y_tup(self):
        """tuple as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, ())

    def test_y_list(self):
        """list as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, [])

    def test_y_float(self):
        """float as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 3.14159)

    def test_y_none(self):
        """none as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, None)

    def test_y_set(self):
        """set as y"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10, {1})


if __name__ == "__main__":
    """main"""
    unittest.main()
