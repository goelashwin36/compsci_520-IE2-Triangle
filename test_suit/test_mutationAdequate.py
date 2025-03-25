import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):

   
    def test_invalids(self):
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1,-1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1,1, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1,10, 12), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3,3, 6), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(6,3, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3,6, 3), Triangle.Type.INVALID)
    
    def test_isoceles(self):
        self.assertEqual(Triangle.classify(1, 2, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 3, 3), Triangle.Type.ISOSCELES)
    
    def test_scalenes(self):
        self.assertEqual(Triangle.classify(6, 7, 8), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(9, 10, 11), Triangle.Type.SCALENE)

    def test_equilaterals(self):
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(4, 4, 4), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(7, 7, 7), Triangle.Type.EQUILATERAL)
    