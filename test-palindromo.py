
import unittest
import main
from main import palindromo

#UNITTEST
class PalindromoUnittest(unittest.TestCase):

    def test_hola(self):
        self.assertFalse(palindromo('hola'))

    def test_ana(self):
        self.assertTrue(palindromo('ana'))
    
    def test_neuquen(self):
        self.assertTrue(palindromo('neuquen'))
    
    def test_reconocer(self):
        self.assertTrue(palindromo('reconocer'))

    def test_auto(self):
        self.assertTrue(palindromo('auto'))

if __name__=='__main__':
    unittest.main()
