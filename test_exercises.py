import unittest
import exercises 

class Test(unittest.TestCase):
    
    def test_exercise_1(self):
        # Check if 'x' is defined
        self.assertTrue(hasattr(exercises, 'x'), "Übung 1 ist fehlgeschlagen: 'x' ist nicht definiert.")
        # Check if 'x' has the correct value
        self.assertEqual(exercises.x, 7, "Übung 1 ist fehlgeschlagen: Der Wert von 'x' sollte 5 sein.")

if __name__ == '__main__':
    unittest.main()