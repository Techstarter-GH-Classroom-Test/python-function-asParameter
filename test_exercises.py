import unittest
from exercises import anwenden

class Test(unittest.TestCase):

    def test_anwenden_multiplikation(self):
        result = anwenden([1, 2, 3], lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6], "Fehler: Multiplikation auf Listenelemente funktioniert nicht korrekt.")

    def test_anwenden_addition(self):
        result = anwenden([5, 10], lambda x: x + 3)
        self.assertEqual(result, [8, 13], "Fehler: Addition auf Listenelemente funktioniert nicht korrekt.")

if __name__ == '__main__':
    unittest.main()
