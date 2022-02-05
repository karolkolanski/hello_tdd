from selenium import webdriver
from time import sleep
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Przed testwem otwieramy stronę
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.maximize_window()

    def tearDown(self):
        # Po teście wyłączamy przeglądarke
        self.driver.quit()

    def testinvalidEmail(self):
        # KROKI
        # 1. Kliknij Zarejestruj - otwiera się strona rejestracji
        pass


if __name__ =="__main__":
    unittest.main()