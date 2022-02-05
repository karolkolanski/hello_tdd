# Test jednostkowy
import unittest

# Tworzymy klasę testową,
# która dziedziczy po klasie TestCase z unittesta
class TestHello(unittest.TestCase):
    # Przygotowanie testów
    def setUp(self):
        print("setup")
    # Zakończenie testów
    def tearDown(self):
        print("teardown")
    # TESTY:
    def testHello(self):
        print("test nr 1")

    def testBye(self):
        print("test nr 2")

# Sprawdzam, czy uruchamiam z tego pliku
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()