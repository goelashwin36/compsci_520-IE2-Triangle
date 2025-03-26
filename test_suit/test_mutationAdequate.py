import unittest
from isTriangle import Triangle


class TriangleTest(unittest.TestCase):

    def test_invalids(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, -1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(1, 1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(-1, 10, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 3, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(6, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        actual = Triangle.classify(3, 6, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_isoceles(self):
        actual = Triangle.classify(1, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        actual = Triangle.classify(5, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_scalenes(self):
        actual = Triangle.classify(6, 7, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        actual = Triangle.classify(9, 10, 11)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_equilaterals(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

        actual = Triangle.classify(4, 4, 4)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

        actual = Triangle.classify(7, 7, 7)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
