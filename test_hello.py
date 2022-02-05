# Test jednostkowy
import unittest
from hello import ProgramHello

# Tworzymy klasę testową,
# która dziedziczy po klasie TestCase z unittesta
class TestProgramHello(unittest.TestCase):
    # Przygotowanie testów
    def setUp(self):
        # Tworzymy instancję klasy ProgramHello
        self.program = ProgramHello()
    # Zakończenie testów
    def tearDown(self):
        print("teardown")
    # TESTY:
    def testHello(self):
        expected = "Hello, world!"
        actual = self.program.welcome()
        self.assertEqual(expected, actual)

# Sprawdzam, czy uruchamiam z tego pliku
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()