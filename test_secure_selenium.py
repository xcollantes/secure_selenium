# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import unittest
import time
from secure_selenium import SecureSelenium


class TestSecureSelenium(unittest.TestCase):
    def setUp(self):
        self.secure = SecureSelenium(
            "", False)

    def test_initial_driver(self):
        self.secure.get("https://gonzaga.edu")
        time.sleep(5)
        self.assertTrue(True)

    def tearDown(self):
        self.secure.close()
