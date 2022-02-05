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
        #2. Wpisz imię
        name_input = driver.find_element(By.ID, "firstname")
        name_input.send_keys("Marcin")
        # 3. Wpisz nazwisko
        lastname_input = driver.find_element(By.ID, "lastname")
        lastname_input.send_keys("Nowak")
        # 4. Wpisz niepoprawny e-mail
        email_input = driver.find_element(By.ID, "email_address")
        email_input.send_keys("jhdjdshjfhdsj.jhjk")

        # UWAGA! TUTAJ BĘDZIE TEST!
        # Klikam w nazwisko
        lastname_input.click()
        # Odszukuję wyświetlone komunikaty o błędach
        errors = driver.find_elements(By.XPATH, '//span[@class="help-block form-error"]')
        # Sprawdzam, czy jest widoczny jeden błąd
        self.assertEqual(1, len(errors))
        # Sprawdzam treść komunikatu
        error = errors[0]
        self.assertEqual("Wprowadzono niepoprawny adres e-mail", error.text)

        # Poczekaj chwilę, żeby zobaczyć co się dzieje
        sleep(4)



if __name__ =="__main__":
    unittest.main()