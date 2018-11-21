import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait


class Wrapper(object):  # pattern SINGLETON
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def remote_webdriver(self, *args, **kwargs):
        self.connection = Firefox()
        return self.connection


class Element(object):
    def __init__(self, locator):
        self._locator = locator


class TextElement(Element):
    def __set__(self, obj, val):
        e = Wrapper().connection.find_element_by_name(self._locator)
        e.send_keys(val)

    def __get__(self, obj, cls=None):
        try:
            e = Wrapper().connection.find_element_by_name(self._locator)
            return str(e.text)
        except Exception as err:
            raise err


class LinkElement(Element):
    def __get__(self, obj, cls=None):
        try:
            WebDriverWait(Wrapper().connection, 30).until(lambda driver: driver.find_element_by_xpath(self._locator))
            e = Wrapper().connection.find_element_by_name(self._locator)
            return str(e.text)
        except Exception as err:
            raise err


class GoogleHomePage(object):
    _url = "http://google.com"
    locators = {
        "search": "q",
        "first_link": "(//a[ancestor::div/@id='ires'])[1]"
    }
    search = TextElement(locators["search"])
    first_link = LinkElement(locators["first_link"])

    def open(self):
        Wrapper().connection.get(self._url)


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Wrapper().remote_webdriver()  # Firefox()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()


class GoogleTesting(BaseTestCase):
    def test_search1(self, page=GoogleHomePage()):
        # page = GoogleHomePage()
        page.open()
        page.search = "Automated testing"
        assert "Test automation" in page.first_link