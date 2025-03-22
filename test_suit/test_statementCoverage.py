import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle


class TriangleTest(unittest.TestCase):
    def test_is_equilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_is_invalid1(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_is_invalid2(self):
        actual = Triangle.classify(-2, 0, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_is_isosceles1(self):
        actual = Triangle.classify(2, 2, 1)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_is_isosceles2(self):
        actual = Triangle.classify(1, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_is_isosceles3(self):
        actual = Triangle.classify(2, 1, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_is_scalene1(self):
        actual = Triangle.classify(2, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_is_scalene2(self):
        actual = Triangle.classify(2, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
