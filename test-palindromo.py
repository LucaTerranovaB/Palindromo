import unittest
from main import palindromo

#UNITTEST
class PalindromoUnittest(unittest.TestCase):

    def test_hola(self):
        palabra = palindromo("hola")
        self.assertFalse(palabra)

    def test_ana(self):
        palabra = palindromo("ana")
        self.assertTrue(palabra)
    
    def test_neuquen(self):
        palabra = palindromo("neuquen")
        self.assertTrue(palabra)
    
    
    def test_reconocer(self):
        palabra = palindromo("reconocer")
        self.assertTrue(palabra)
    

    def test_auto(self):
        palabra = palindromo("auto")
        self.assertFalse(palabra)
    

if __name__=='__main__':
    unittest.main()
