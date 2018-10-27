
import unittest


class OutClass(unittest.TestCase):

    def test_01(self):
        self.assertNotEquals(4, 7)
        return

    def test_02(self):
        self.assertEquals(7, 7)
        return


test_01 = OutClass("test_01")
test_02 = OutClass("test_02")

suite1 = unittest.TestLoader([test_01, test_02])
suite1.run(result)

print(result)

suite2 = unittest.TestLoader().loadTestsFromTestCase(OutClass)
suite2.run(result)
print(result)
