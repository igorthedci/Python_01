
import unittest


class OutClass(unittest.TestCase):

    def test_01(self):
        self.assertNotEquals(4, 7)

    def test_02(self):
        self.assertEquals(7, 7)


unittest.main()
