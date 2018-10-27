import unittest


class OurClass(unittest.TestCase):

    def test_02(self):
        nums = [1, 2, 5, 8]
        for n in nums:
            with self.subTest(number=n):
                self.assertEqual(number % 2, 0)


if __name__ == '__main__':
    unittest.main()