import requests
import unittest


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = r"http://pulse-rest-testing.herokuapp.com"

    def test_base_url(self):
        responce = requests.get(self.base_url)
        self.assertEqual(200, responce.status_code)
        responce_body = responce.json()
        self.assertEqual(2, len(responce_body))
        expected_dict = {"Roles": self.base_url+"/roles", "Books": self.base_url+"/books"}
        self.assertDictEqual(expected_dict, responce_body)


if __name__ == '__main__':
    pass
#