from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Przed testwem otwieramy stronę
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.driver.maximize_window()
        accept_button = self.driver.find_element(By.XPATH, '//button[@data-testid="permission-popup-accept"]')
        accept_button.click()

    def tearDown(self):
        # Po teście wyłączamy przeglądarkę
        self.driver.quit()

    def testinvalidEmail(self):
        # KROKI
        # 1. Kliknij Zarejestruj - otwiera się strona rejestracji
        driver = self.driver
        register_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Zarejestruj")
        register_btn.click()
        # Poczekaj chwilę, żeby zobaczyć co się dzieje
        sleep(4)



if __name__ =="__main__":
    unittest.main()