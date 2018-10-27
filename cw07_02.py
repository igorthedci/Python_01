
import unittest
from HtmlTestRunner import HTMLTestRunner


class OutClass(unittest.TestCase):

    def test_01(self):
        self.assertNotEqual(4, 7)

    def test_02(self):
        self.assertEqual(7, 7)


# unittest.main()
# unittest.main(testRunner=HTMLTestRunner(output=r"./"))
unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"./"))
