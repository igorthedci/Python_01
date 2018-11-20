import unittest
from Selenium.webdriver import Firefox


class Wrapper(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def remote_webdriver(self, *args, **kwargs):
        self.connection = Firefox()
        return self.connection


class GoogleHomePage(object):
    def open(self):
        Wrapper().connection.get(self._url)


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.driver.implicity.wait(30)

    def tearDown(self):
        self.driver.close()


class GoogleTesting(BaseTestCase):

    def test_search(self):
        page = GoogleHomePage()
        page.open()
        page.search = "Automation testing"
        assert "Test automation" in page.first_link