import unittest
import math
from Vector import Vector

class TestVector(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector(2, 3, 5)
        self.v2 = Vector(1, 2, 3)
        self.v3 = Vector(2, 3, 5)

    def test_init(self):
        self.assertEqual(self.v1.x, 2)
        self.assertEqual(self.v1.y, 3)
        self.assertEqual(self.v1.z, 5)

    def test_repr(self):
        self.assertEqual(repr(self.v1), "Vector(2, 3, 5)")

    def test_eq(self):
        self.assertEqual(self.v1, self.v3)

    def test_ne(self):
        self.assertNotEqual(self.v1, self.v2)

    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(result, Vector(3, 5, 8))

    def test_sub(self):
        result = self.v1 - self.v2
        self.assertEqual(result, Vector(1, 1, 2))

    def test_mul(self):
        result = self.v1 * self.v2
        self.assertEqual(result, 23)

    def test_cross(self):
        result = self.v1.cross(self.v2)
        self.assertEqual(result, Vector(-1, -1, 1))

    def test_length(self):
        result = self.v1.length()
        self.assertEqual(result, math.sqrt(38))

    def test_hash(self):
        self.assertEqual(hash(self.v1), hash((2, 3, 5)))

    def tearDown(self):
        print("cleaning")

if __name__ == '__main__':
    unittest.main()
