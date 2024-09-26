import unittest
from notenberechnung import berechne_prozentwert, bestimme_note, func

class TestFunktionen(unittest.TestCase):

    def test_berechne_prozentwert_positive(self):
        self.assertEqual(berechne_prozentwert(90, 100), 90.0)  
        self.assertEqual(berechne_prozentwert(50, 200), 25.0) 
        self.assertEqual(berechne_prozentwert(75, 300), 25.0) 

    def test_berechne_prozentwert_negative(self):
        with self.assertRaises(ZeroDivisionError):
            berechne_prozentwert(50, 0) 
        self.assertEqual(berechne_prozentwert(-50, 100), -50.0) 

    def test_bestimme_note_positive(self):
        self.assertEqual(bestimme_note(95), "sehr gut")
        self.assertEqual(bestimme_note(85), "gut")
        self.assertEqual(bestimme_note(70), "befriedigend")
        self.assertEqual(bestimme_note(55), "ausreichend")
        self.assertEqual(bestimme_note(30), "ungenügend")

    def test_bestimme_note_negative(self):
        self.assertEqual(bestimme_note(-10), "ungenügend") 
        self.assertEqual(bestimme_note(120), "sehr gut") 

    def test_func_positive(self):
        self.assertEqual(func("123"), "123") 

    def test_func_negative(self):
        with self.assertRaises(ValueError):
            func("abc")
        with self.assertRaises(ValueError):
            func("12.34")  


if __name__ == "__main__":
    unittest.main()
