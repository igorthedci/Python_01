import unittest
from distance import distance_two_dots


class DistanceTests(unittest.TestCase):

    def test_zero(self):
        res = distance_two_dots(0,0,0,0)
        self.assertEqual(res, 0)

    def test_01(self):
        res = distance_two_dots(1, -1, 1, -1)
        self.assertEqual(res, 0)

    def test_02(self):
        res = distance_two_dots(0, 0, -3, -4)
        self.assertEqual(res, 5.)

    def test_03(self):
        res = distance_two_dots(-5, 12, 0, 0)
        self.assertEqual(res, 13.)

    def test_04(self):
        res = distance_two_dots(5.5, 12.5, 0.5, 0.5)
        self.assertEqual(res, 13)

    def test_05(self):
        res = distance_two_dots(3, 4, 5, 6)
        self.assertEqual(res, 8**0.5)

    def test_06(self):
        res = distance_two_dots(3, 4, 5, 6)
        self.assertNotEqual(res, 1)

#
if __name__ == '__main__':
    unittest.main()
#